#!/usr/bin/env python
import sys
from numpy import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt;
plt.rcdefaults()
plt.style.use('bmh')
import numpy as np

def population_plot(case_name, dynamic, fnames, enemy):
    tasks = []
    for fname in fnames:
        with open(fname, 'r') as f:
            lines = f.readlines()
            tasks.append(map(float, filter(None, lines[0].strip().split(' '))))

    # print tasks

    i = 0
    simple_tasks = []
    while i < len(tasks):
        j = 0
        simple_tasks.append([])
        while j < len(tasks[i]):
            simple_tasks[i].append(sum(tasks[i][j:j + 3]))
            j += 3
        #print simple_tasks[i]
        i += 1


    # Calculate averages over fnames
    simple_tasks = np.array(simple_tasks)
    #ave_tasks = np.sum(simple_tasks, axis=0)
    print simple_tasks
    print '\n'
    #Ignore noones - that is request/attempts when noone was known
    #ave_tasks[0] = ave_tasks[0] - ave_tasks[6]
    #ave_tasks[1] = ave_tasks[1] - ave_tasks[6]
    #ave_tasks[4] = ave_tasks[4] - ave_tasks[6]
    #print ave_tasks
    
    width = 0.4
    if enemy == 0 or enemy == 1:
        
        one_agent = simple_tasks[0,:]
        print one_agent
        one_agent[0] = one_agent[0] - one_agent[6]
        one_agent[1] = one_agent[1] - one_agent[6]
        one_agent[4] = one_agent[4] - one_agent[6]
        print '\n'
        rest = simple_tasks[1:,:]
        print rest
        ave_rest = np.sum(rest, axis=0)
        ave_rest[0] = ave_rest[0] - ave_rest[6]
        ave_rest[1] = ave_rest[1] - ave_rest[6]
        ave_rest[4] = ave_rest[4] - ave_rest[6]
        ave_rest = ave_rest / (len(simple_tasks) - 1)
        
        #write to file the two rows with values
        with open('out', 'w') as f:
            for x in one_agent:
                f.write(str(x)+' ')
            f.write('\n')
            for x in ave_rest:
                f.write(str(x)+' ')
            
        print len(simple_tasks) - 1
        fig = plt.figure()
        #
        plt.subplot(2, 2, 1)
        #objects = ('a', 'da', 'c', 'dc', 'sa', 'sc', 'cn', 'rq', 'rS', 'rR', 'rRA', 'rRS')
        objects = ('c/nc', 'dc/dnc', 'sc/snc', 'rS/rSS', 'rR/rRA', 'rRA/rRS')
        y_pos = np.arange(len(objects))
        completed = (one_agent[2], one_agent[3], one_agent[5], one_agent[8], one_agent[10], one_agent[11])
        notcompleted = (one_agent[0] - one_agent[2], one_agent[1] - one_agent[3], one_agent[4] - one_agent[5], one_agent[7] - one_agent[8], one_agent[9] - one_agent[10], one_agent[10] - one_agent[11])
        ind = np.arange(len(completed))
        p1 = plt.bar(ind, completed, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, notcompleted, width, bottom=completed, align='center', alpha=0.5)
        #plt.bar(y_pos, one_agent[0:12], align='center', alpha=0.5)
        
        plt.xticks(y_pos, objects)
        plt.ylabel('Nr of tasks')
        plt.title('1 agent')
        plt.tight_layout()
        plt.xticks(rotation=30)
        
        plt.subplot(2, 2, 3)
        #depend_own = (one_agent[12], one_agent[13], one_agent[10], one_agent[11], one_agent[8])
        #depend_not_own = (one_agent[1] - one_agent[12], one_agent[3] - one_agent[13], one_agent[9] - one_agent[10], one_agent[10] - one_agent[11], one_agent[7] - one_agent[8])
        depend_own = (one_agent[12], one_agent[13])
        depend_not_own = (one_agent[1] - one_agent[12], one_agent[3] - one_agent[13])
        ind = np.arange(len(depend_own))
            
        p1 = plt.bar(ind, depend_own, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, depend_not_own, width, bottom=depend_own, align='center', alpha=0.5)
        plt.ylabel('Nr of tasks')
        #plt.xticks(ind, ('daO/daNO', 'dcO/dcNO', 'rA/rNA', 'rS/rNS', 'rS/rSe'))
        plt.xticks(ind, ('daO/daNO', 'dcO/dcNO'))
        plt.tight_layout()
        plt.xticks(rotation=30)
        
        ax1 = plt.subplot(2, 2, 2)
        
        ax1.yaxis.tick_right()
        #plt.bar(y_pos, ave_rest[0:12], align='center', alpha=0.5)
        completed = (ave_rest[2], ave_rest[3], ave_rest[5], ave_rest[8], ave_rest[10], ave_rest[11])
        notcompleted = (ave_rest[0] - ave_rest[2], ave_rest[1] - ave_rest[3], ave_rest[4] - ave_rest[5], ave_rest[7] - ave_rest[8], ave_rest[9] - ave_rest[10], ave_rest[10] - ave_rest[11])
        ind = np.arange(len(completed))
        p1 = plt.bar(ind, completed, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, notcompleted, width, bottom=completed, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Nr of tasks')
        plt.title('Average agents')
        plt.tight_layout()
        plt.xticks(rotation=30)
        
        ax1 = plt.subplot(2, 2, 4)
        ax1.yaxis.tick_right()
        #depend_own = (ave_rest[12], ave_rest[13], ave_rest[10], ave_rest[11], ave_rest[8])
        #depend_not_own = (ave_rest[1] - ave_rest[12], ave_rest[3] - ave_rest[13], ave_rest[9] - ave_rest[10], ave_rest[10] - ave_rest[11], ave_rest[7] - ave_rest[8])
        depend_own = (ave_rest[12], ave_rest[13])
        depend_not_own = (ave_rest[1] - ave_rest[12], ave_rest[3] - ave_rest[13])
        ind = np.arange(len(depend_own))
            
        p1 = plt.bar(ind, depend_own, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, depend_not_own, width, bottom=depend_own, align='center', alpha=0.5)
        plt.ylabel('Nr of tasks')     
        plt.xticks(ind, ('daO/daNO', 'dcO/dcNO'))
        #fig.autofmt_xdate()
        plt.tight_layout()
        plt.xticks(rotation=30)
        fig.savefig(case_name+'.jpg')
    else:
        
        one_half = simple_tasks[0:len(simple_tasks)/2,:]
        print one_half
        one_ave = np.sum(one_half, axis=0)
        print one_ave
        print '\n'
        second_half = simple_tasks[len(simple_tasks)/2:,:]
        print second_half
        second_ave = np.sum(second_half, axis=0)

        print second_ave
        
        one_ave[0] = one_ave[0] - one_ave[6]
        one_ave[1] = one_ave[1] - one_ave[6]
        one_ave[4] = one_ave[4] - one_ave[6]
        
        second_ave[0] = second_ave[0] - second_ave[6]
        second_ave[1] = second_ave[1] - second_ave[6]
        second_ave[4] = second_ave[4] - second_ave[6]
        
        one_ave = 2*one_ave / len(simple_tasks)
        second_ave = 2*second_ave / len(simple_tasks)
        print len(simple_tasks)/2
        
        #write to file the two rows with values
        with open('out', 'w') as f:
            for x in one_ave:
                f.write(str(x)+' ')
            f.write('\n')
            for x in second_ave:
                f.write(str(x)+' ')
        fig = plt.figure()
        #
        plt.subplot(2, 2, 1)
        objects = ('c/nc', 'dc/dnc', 'sc/snc', 'rS/rSS', 'rR/rRA', 'rRA/rRS')
        y_pos = np.arange(len(objects))
        completed = (one_ave[2], one_ave[3], one_ave[5], one_ave[8], one_ave[10], one_ave[11])
        notcompleted = (one_ave[0] - one_ave[2], one_ave[1] - one_ave[3], one_ave[4] - one_ave[5], one_ave[7] - one_ave[8], one_ave[9] - one_ave[10], one_ave[10] - one_ave[11])
        ind = np.arange(len(completed))
        p1 = plt.bar(ind, completed, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, notcompleted, width, bottom=completed, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Nr of tasks')
        plt.title('First ave')
        plt.tight_layout()
        plt.xticks(rotation=30)
        
        plt.subplot(2, 2, 3)
        depend_own = (one_ave[12], one_ave[13])
        depend_not_own = (one_ave[1] - one_ave[12], one_ave[3] - one_ave[13])
        ind = np.arange(len(depend_own))
            
        p1 = plt.bar(ind, depend_own, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, depend_not_own, width, bottom=depend_own, align='center', alpha=0.5)
        plt.ylabel('Nr of tasks')
        plt.xticks(ind, ('daO/daNO', 'dcO/dcNO'))
        plt.tight_layout()
        plt.xticks(rotation=30)
        
        ax1 = plt.subplot(2, 2, 2)
        
        ax1.yaxis.tick_right()
        completed = (second_ave[2], second_ave[3], second_ave[5], second_ave[8], second_ave[10], second_ave[11])
        notcompleted = (second_ave[0] - second_ave[2], second_ave[1] - second_ave[3], second_ave[4] - second_ave[5], second_ave[7] - second_ave[8], second_ave[9] - second_ave[10], second_ave[10] - second_ave[11])
        ind = np.arange(len(completed))
        p1 = plt.bar(ind, completed, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, notcompleted, width, bottom=completed, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Nr of tasks')
        plt.title('Second ave')
        plt.tight_layout()
        plt.xticks(rotation=30)
        
        ax1 = plt.subplot(2, 2, 4)
        ax1.yaxis.tick_right()
        depend_own = (second_ave[12], second_ave[13])
        depend_not_own = (second_ave[1] - second_ave[12], second_ave[3] - second_ave[13])
        ind = np.arange(len(depend_own))
        #width = 0.35
            
        p1 = plt.bar(ind, depend_own, width, align='center', alpha=0.5)
        p2 = plt.bar(ind, depend_not_own, width, bottom=depend_own, align='center', alpha=0.5)
        plt.ylabel('Nr of tasks')     
        plt.xticks(ind, ('daO/daNO', 'dcO/dcNO'))
        #fig.autofmt_xdate()
        plt.tight_layout()
        plt.xticks(rotation=30)
        fig.savefig(case_name+'.jpg')

def plot_depend_own(case_name, fnames):
    tasks = []
    for fname in fnames:
        with open(fname, 'r') as f:
            lines = f.readlines()
            tasks.append(map(float, filter(None, lines[0].strip().split(' '))))

    # print tasks
    i = 0
    simple_tasks = []
    while i < len(tasks):
        j = 0
        simple_tasks.append([])
        while j < len(tasks[i]):
            simple_tasks[i].append(sum(tasks[i][j:j + 3]))
            j += 3
        print simple_tasks[i]
        i += 1

    # Calculate averages over fnames
    simple_tasks = np.array(simple_tasks)
    
    no = 1
    for x in simple_tasks:
        fig = plt.figure()
        plt.subplot(2, 1, 1)
        temp = [x[0], x[1], x[2], x[3], x[12], x[13], x[9], x[10], x[11]]
        objects = ('ta', 'tda', 'tc', 'tdc', 'tdoa', 'tdoc', 'r_r', 'r_ra', 'r_rs')
        y_pos = np.arange(len(objects))
        plt.bar(y_pos, temp, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Value')
        plt.title('Preliminary')
        
        plt.subplot(2, 1, 2)
        depend_own = (x[12], x[13], x[10], x[11], x[8])
        depend_not_own = (x[1] - x[12], x[3] - x[13], x[9] - x[10], x[10] - x[11], x[7] - x[8])
        ind = np.arange(len(depend_own))
        width = 0.35
            
        p1 = plt.bar(ind, depend_own, width, color='blue', align='center', alpha=0.5)
        p2 = plt.bar(ind, depend_not_own, width, color='green', bottom=depend_own, align='center', alpha=0.5)
        ''' 
        req_acc = (x[10])
        req_not_acc = (x[9] - x[10])
        ind = np.arange(2)
        width = 0.1
        
        p1 = plt.bar(ind, req_acc, width, color='blue', align='center', alpha=0.5)
        p2 = plt.bar(ind, req_not_acc, width, color='green', bottom=req_acc, align='center', alpha=0.5)
        
        req_suc = (x[11])
        req_not_suc = (x[10] - x[11])
        ind = np.arange(2)
        width = 0.1
        
        p1 = plt.bar(ind, req_suc, width, color='blue', align='center', alpha=0.5)
        p2 = plt.bar(ind, req_not_suc, width, color='green', bottom=req_suc, align='center', alpha=0.5)
        
        req_own_suc = (x[8])
        req_own_not_suc = (x[7] - x[8])
        ind = np.arange(2)
        width = 0.1
        
        p1 = plt.bar(ind, req_own_suc, width, color='blue', align='center', alpha=0.5)
        p2 = plt.bar(ind, req_own_not_suc, width, color='green', bottom=req_own_suc, align='center', alpha=0.5)
        '''           
        plt.ylabel('Nr of tasks')
        plt.title('Depend task completion')
        plt.xticks(ind, ('attempt', 'complete', 'racc/rnacc', 'rsuc/rnsuc', 'rosucc/sent'))
        #plt.yticks(np.arange(0, 81, 10))
        #plt.legend(loc='upper center', (p1[0], p2[0]), ('Own', 'Not Own'))
        fig.savefig(str(no)+'_'+case_name+'_tasks_depend.jpg')
        no += 1
  
def plot_delta_gamma(case_name, fnames):
    pieces = []
    for fname in fnames:
        with open(fname, 'r') as f:
            lines = f.readlines()
            pieces.append(filter(None, lines[6].strip().split(',')))

    no = 0
    for y in pieces:
        points = []
        for x in y:
            points.append(filter(None, x.split(' ')))
        # print points
        # Plot the points
        fig = plt.figure()
        i = 0
        gamma = []
        delta = []
        gamma_p = []
        delta_p = []
        for point in points:
            if point[0] == '0':
                delta.append(float(point[1]))
                delta_p.append(float(point[3]))
            else:
                gamma.append(float(point[1]))
                gamma_p.append(float(point[3]))
            i += 1   
        
        delta = np.array(delta)
        delta_p = np.array(delta_p)
        gamma = np.array(gamma)
        gamma_p = np.array(gamma_p) 

        plt.subplot(2,1,1)
        plt.plot(np.arange(len(delta)), delta, c='green')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.plot(np.arange(len(delta)), delta_p, c='red')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.subplot(2,1,2)
        plt.plot(np.arange(len(gamma)), gamma, c='blue')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.plot(np.arange(len(gamma)), gamma_p, c='red')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 

        no = no + 1
        plt.suptitle("All tasks")
        fig.savefig(str(no) +'_' + case_name + '_all_delta_gamma_mu.jpg')

        fig = plt.figure()
        i = 0
        gamma = []
        delta = []
        gamma_p = []
        delta_p = []
        for point in points:
            if point[0] == '0':
                delta.append(float(point[1]))
                delta_p.append(float(point[4]))
            else:
                gamma.append(float(point[1]))
                gamma_p.append(float(point[4]))
            i += 1   
        
        delta = np.array(delta)
        delta_p = np.array(delta_p)
        gamma = np.array(gamma)
        gamma_p = np.array(gamma_p) 

        plt.subplot(2,1,1)
        plt.plot(np.arange(len(delta)), delta, c='green')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.plot(np.arange(len(delta)), delta_p, c='red')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.subplot(2,1,2)
        plt.plot(np.arange(len(gamma)), gamma, c='blue')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.plot(np.arange(len(gamma)), gamma_p, c='red')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 

        plt.suptitle("Depend tasks")
        fig.savefig(str(no) +'_' + case_name + '_depend_delta_gamma_mu.jpg')

        fig = plt.figure()
        i = 0
        gamma = []
        delta = []
        gamma_p = []
        delta_p = []
        for point in points:
            if point[0] == '0':
                delta.append(float(point[1]))
                delta_p.append(float(point[5]))
            else:
                gamma.append(float(point[1]))
                gamma_p.append(float(point[5]))
            i += 1   
        
        delta = np.array(delta)
        delta_p = np.array(delta_p)
        gamma = np.array(gamma)
        gamma_p = np.array(gamma_p) 

        plt.subplot(2,1,1)
        plt.plot(np.arange(len(delta)), delta, c='green')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.plot(np.arange(len(delta)), delta_p, c='red')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.subplot(2,1,2)
        plt.plot(np.arange(len(gamma)), gamma, c='blue')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 
        
        plt.plot(np.arange(len(gamma)), gamma_p, c='red')
        axes = plt.gca()
        axes.set_ylim([-0.5,1.5]) 

        plt.suptitle("Depend tasks")
        fig.savefig(str(no) +'_' + case_name + '_own_delta_gamma_mu.jpg')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: ./plot_2.py static/dynamic case_name filename enemy'
        sys.exit()

    name_of_files = []
    for x in range(4, len(sys.argv)):
        name_of_files.append(sys.argv[x])

    population_plot(sys.argv[2], sys.argv[1], name_of_files, int(sys.argv[3]))
