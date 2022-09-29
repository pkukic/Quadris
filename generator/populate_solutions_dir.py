import cplex
import sys
import os

from cplex.callbacks import IncumbentCallback
from matlab import engine as matlab_engine
from sqlib import run_insert, run_select, sum_of_indices


class ReportCallback(IncumbentCallback):
    def __init__(self, env):
        super().__init__(env)

        self.i = len(os.listdir('../unique/colors/'))
        self.rejected = 0
        self.db_path = '../unique/polyminoes.db'
        self.eng = matlab_engine.start_matlab()

    def __call__(self):
        x = super().get_values(["x" + str(i + 1) for i in range(1149)])
        x = [abs(item) for item in x]
        
        r_color, r_label = self.eng.color_and_label_for_quadris(x, nargout=2)
        ro1, ro2, ro3, ro4, mu1, mu2, delta1, delta2 = self.eng.reflections_and_symmetries(r_color, nargout=8)
        
        flag = 0
        
        for mat in [ro1, ro2, ro3, ro4, mu1, mu2, delta1, delta2]:
            sumofi = sum_of_indices(mat)
            selected = run_select(self.db_path, sumofi)['table']
            print(selected)
            if len(selected) != 0 and self.eng.check_if_in_unique(r_color, [row[0] for row in selected], nargout=1):
                flag += 1
        
        flag = 1 if flag > 0 else 0
        
        if not flag:
            self.i += 1
            fname = f'./unique/colors/r_color_{self.i}.mat'
            print(f"Unique solutions so far: {self.i}")
            self.eng.save_color_matrix(r_color, self.i, nargout=0)
            self.eng.save_label_matrix(r_label, self.i, nargout=0)
            self.eng.save_plots(self.i,self.i,nargout=0)
        
            run_insert(self.db_path, sumofi, fname)
            
        else:
            self.rejected += 1


def get_solutions(input_filename, N=1000):
    c = cplex.Cplex(input_filename)
    c.parameters.mip.pool.absgap.set(0.0)
    c.parameters.mip.pool.intensity.set(4)
    c.parameters.mip.limits.populate.set(int(N))
    c.parameters.mip.pool.capacity.set(int(N))
    c.parameters.output.writelevel.set(1)
    c.register_callback(ReportCallback)
    c.populate_solution_pool()
    

if __name__ == '__main__':
    args = sys.argv
    fname = args[1]
    data = args[2:]
    globals()[fname](*data)
