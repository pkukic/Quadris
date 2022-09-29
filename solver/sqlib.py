import numpy as np
import sqlite3
import sys

def sum_of_indices(r_color):
    
    r_color = np.asarray(r_color)
    sumofi = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    for i in range(1, 6+1):
        rows, cols = (r_color == i).nonzero()
        rows *= 9
        indices = rows + cols
        sumofi[i] = sum(indices)
    return sumofi


def run_sqlite(db_path: str, query: str, ignore_output = None) -> dict:
    try:
        conn = sqlite3.connect(db_path)
    except BaseException:
        sys.exit(f"Error connecting to database {db_path}")
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except BaseException:
        sys.exit(f"Error executing query: \n{query}\n to database")
    
    if not ignore_output:
        table = cursor.fetchall()
        headers = list(map(lambda x: x[0], cursor.description))
        conn.close()

        table_with_description = {'table': table, 'headers': headers}
        return table_with_description
    else:
        conn.commit()
        conn.close()


def select_all(sumofi):
    return f"""
    SELECT * FROM sums WHERE
    shape_1 = {sumofi[1]} AND
    shape_2 = {sumofi[2]} AND
    shape_3 = {sumofi[3]} AND
    shape_4 = {sumofi[4]} AND
    shape_5 = {sumofi[5]} AND
    shape_6 = {sumofi[6]};
    """

def select_duplicates():
    return """
        select s1.fname, s2.fname
        from sums as s1
        join sums as s2
        on s1.shape_1 = s2.shape_1 and
            s1.shape_2 = s2.shape_2 and 
            s1.shape_3 = s2.shape_3 and
            s1.shape_4 = s2.shape_4 and 
            s1.shape_5 = s2.shape_5 and
            s1.shape_6 = s2.shape_6 and 
            s1.fname != s2.fname
    """

def select_greater_than(sumofi):
    print("in select greater than")
    print(sumofi)
    query = f"""
    SELECT * FROM sums WHERE
    shape_1 >= {sumofi[1]} AND
    shape_2 >= {sumofi[2]} AND
    shape_3 >= {sumofi[3]} AND
    shape_4 >= {sumofi[4]} AND
    shape_5 >= {sumofi[5]} AND
    shape_6 >= {sumofi[6]};
    """
    print(query)
    return query

def insert(sumofi, fname):
    return f"""
    INSERT INTO sums (shape_1, shape_2, shape_3, shape_4, shape_5, shape_6, fname)
    VALUES ({sumofi[1]}, {sumofi[2]}, {sumofi[3]}, {sumofi[4]}, {sumofi[5]}, {sumofi[6]}, '{fname}');
    """

def run_select(db_path, sumofi):
    return run_sqlite(db_path, select_all(sumofi))


def run_insert(db_path, sumofi, fname):
    return run_sqlite(db_path, insert(sumofi, fname), ignore_output=True)