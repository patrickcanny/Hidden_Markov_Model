'''
EECS738 - Machine Learning
@file: hmm.py
'''
from tools import FileTools

class HMM():
    def __init__(self, states):
        self.states = states

    def get_emission_prob(self):
        pass

    def get_transition_prob(self):
        pass

    def viterbi(obs, states, start_p, trans_p, emit_p):
        #TODO Implement This Pseudocode
        '''
        for each state in our model's set of states:
            T_1[i,1] = pi_i*B_iy_1
            T_2[i,1] = 0
        end for
        for each observation:
            for each state:
                T_1[j,i] = max_k(T_1[k,i-1]*A_kj*B_jy_i)
                T_2[j,i] = argmax_k(T_1[k,i-1]*A_kj*B_jy_i)
            end for
        end for
        z_T = argmax_k(T_1[k,T])
        x_T = s_Z_T
        for i = T, T-1,...,2:
            z_i-1 = T_2[z_i,i]
            x_i-1 = s_z_i-1
        end for
        return x
        '''
        pass

    def train(self):
        pass

    def predict(self):
        pass

