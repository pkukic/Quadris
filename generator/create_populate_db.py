import sqlite3
import scipy.io as sio
import os

from sum_of_indices import sum_of_indices

conn = sqlite3.connect('../unique/polyminoes.db')
c = conn.cursor()

def sumofi_from_fname(fname):
    r_color = sio.loadmat(fname)['r_color']
    return sum_of_indices(r_color)


c.execute(
    """
    drop table sums;
    """
)

c.execute(
    """
    create table if not exists sums (
        fname text primary key,
        shape_1 integer,
        shape_2 integer,
        shape_4 integer, 
        shape_3 integer,
        shape_5 integer,
        shape_6 integer
    );
    """
)

c.execute(
    """
    create index ind on sums (shape_1, shape_2, shape_3, shape_4, shape_5, shape_6);
    """
)

conn.commit()

dir = '../unique/colors/'
fnames = [os.path.join(dir, fname) for fname in os.listdir(dir)]

for fname in fnames:
    sumofi = sumofi_from_fname(fname)
    c.execute(
        f"""
        insert into sums (shape_1, shape_2, shape_3, shape_4, shape_5, shape_6, fname)
        values ({sumofi[1]}, {sumofi[2]}, {sumofi[3]}, {sumofi[4]}, {sumofi[5]}, {sumofi[6]}, '{fname}')
        """
    )
    print(f"Filled in {fname}")
    conn.commit()