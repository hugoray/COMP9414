"""
9414 Assignment 1 Term 2 2020
written by Shiran Huang z5233229
modify some parts in searchGeneric.py to fulfill the greedy search and ban the display funciton
"""

import sys
from cspProblem import Constraint,CSP
from cspConsistency import Search_with_AC_from_CSP
from searchGeneric import AStarSearcher


# classify a new csp with soft constraints and soft cost based on CSP in cspProblem
class SOFT_CSP(CSP):
    def __init__(self,domains,constraints,soft_constraints,soft_cost):
        super(SOFT_CSP, self).__init__(domains,constraints)
        self.soft_constraints = soft_constraints
        self.soft_cost = soft_cost

# need to add a way with its neighbours
class AC_CSP(Search_with_AC_from_CSP):
    def __init__(self, csp):
        super(AC_CSP, self).__init__(csp)
        self.cost = []
        self.soft_cons = csp.soft_constraints
        self.soft_cost = soft_cost

    # heuristic
    def heuristic(self,node):
        # gather all the min cost into one list
        cost_list = []
        # task node's cost
        for task in node:
            if task in self.soft_cons:
                temp = []
                expect_time = self.soft_cons[task]
                for value in node[task]:
                    actual_time = value[1]
                    if actual_time > expect_time:
                        # delay = actual_time - expect_time
                        delay = (actual_time//10-expect_time//10)*24 + ((actual_time%10) - (expect_time%10))
                        temp.append(self.soft_cost[task] * delay)
                    else:
                        temp.append(0)
                # if temp list not null, add the min one to the cost list
                if len(temp) != 0:
                    cost_list.append(min(temp))

        return sum(cost_list)

# binary constraint
def binary_before(t1,t2):
    return t1[1] <= t2[0]

def binary_after(t1,t2):
    return t2[1] <= t1[0]

def binary_same_day(t1,t2):
    return t1[0]//10 == t2[0]//10

def binary_starts_at(t1,t2):
    return t1[0] == t2[1]

# hard constraint
def hard_day(day):
    def hardday(val):
        return val[0]//10 == day
    return hardday

def hard_time(time):
    def hardtime(val):
        return val[0] % 10 == time
    return hardtime

def sb_day(day,time):
    def sbday(val):
        given_time = day*10 + time
        return val[0] <= given_time
    return sbday

def sb_time(time):
    def sbtime(val):
        return val[0] % 10 <= time
    return sbtime

def sa_day(day,time):
    def saday(val):
        given_time = day * 10 + time
        return val[0] >= given_time
    return saday

def sa_time(time):
    def satime(val):
        return val[0] % 10 >= time
    return satime

def eb_day(day,time):
    def ebday(val):
        given_time = day * 10 + time
        return val[1] <= given_time
    return ebday

def eb_time(time):
    def ebtime(val):
        return val[1] %10 <= time
    return ebtime

def ea_day(day,time):
    def eaday(val):
        given_time = day * 10 + time
        return val[1] >= given_time
    return eaday

def ea_time(time):
    def eatime(val):
        return val[1] %10 >= time
    return eatime

def si_day(day1,time1,day2,time2):
    def siday(val):
        given_time1 = day1*10 +time1
        given_time2 = day2*10 +time2
        return given_time1 <= val[0] <= given_time2

    return siday

def ei_day(day1,time1,day2,time2):
    def eiday(val):
        giventime1 = day1 * 10 + time1
        giventime2 = day2 * 10 + time2
        return giventime1 <= val[1] <= giventime2

    return eiday



# create a week and time dict
week_to_num = {'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5}
time_to_num = {'9am': 1, '10am': 2, '11am':3, '12pm': 4, '1pm': 5, '2pm': 6, '3pm': 7, '4pm': 8, '5pm':9}

# working hours domain set
domain = set()
for i in range (1,6):
    for j in range(1,10):
        domain.add(i*10+j)
domain = sorted(domain)
#print(domain)

task_domain = {}
hard_constraint = []
soft_constraint = {}
soft_cost = {}
task_list = []

# read the input
filename = sys.argv[1]
with open(filename,'r') as f:
    for line in f.readlines():
        #print(line)
        line = line.strip()
        line = line.replace(',', '')
        line = line.split(' ')

        if 'task' in line and '#' not in line:
            aset =set()
            for i in domain:
                if int(line[2]) + i % 10 <= 9:
                    aset.add((i,i+int(line[2])))
            aset =sorted(aset)
            task_domain[line[1]] = aset

        # get binary constraints
        if 'constraint' in line and '#' not in line:
            t1 = line[1]
            t2 = line[3]
            if line[2] == 'before':
                hard_constraint.append(Constraint((t1,t2),binary_before))

            if line[2] == 'after':
                hard_constraint.append(Constraint((t1,t2),binary_after))

            if line[2] == 'same-day':
                hard_constraint.append(Constraint((t1,t2),binary_same_day))

            if line[2] == 'starts-at':
                hard_constraint.append(Constraint((t1,t2),binary_starts_at))

        # get hard constraints by using the definitions above
        if 'domain' in line and 'ends-by' not in line and '#' not in line:
            t = line[1]

            if line[2] in week_to_num:
                day = week_to_num[line[2]]
                hard_constraint.append(Constraint((t,), hard_day(day)))


            if line[2] in time_to_num:
                time = time_to_num[line[2]]
                hard_constraint.append(Constraint((t,), hard_time(time)))

            if 'starts-before' in line:
                if len(line) == 5:
                    if line[3] in week_to_num and line[4] in time_to_num:
                        day = week_to_num[line[3]]
                        time = time_to_num[line[4]]
                        hard_constraint.append(Constraint((t,), sb_day(day,time)))

                else:
                    if line[-1] in time_to_num:
                        time = time_to_num[line[-1]]
                        hard_constraint.append(Constraint((t,), sb_time(time)))

            if 'starts-after' in line:
                if len(line) == 5:
                    if line[3] in week_to_num and line[4] in time_to_num:
                        day = week_to_num[line[3]]
                        time = time_to_num[line[4]]
                        hard_constraint.append(Constraint((t,), sa_day(day,time)))

                else:
                    if line[-1] in time_to_num:
                        time = time_to_num[line[-1]]
                        hard_constraint.append(Constraint((t,), sa_time(time)))

            if 'ends-before' in line:
                if len(line) == 5:
                    if line[3] in week_to_num and line[4] in time_to_num:
                        day = week_to_num[line[3]]
                        time = time_to_num[line[4]]
                        hard_constraint.append(Constraint((t,), eb_day(day, time)))

                else:
                    if line[-1] in time_to_num:
                        time = time_to_num[line[-1]]
                        hard_constraint.append(Constraint((t,), eb_time(time)))

            if 'ends-after' in line:
                if len(line) == 5:
                    if line[3] in week_to_num and line[4] in time_to_num:
                        day = week_to_num[line[3]]
                        time = time_to_num[line[4]]
                        hard_constraint.append(Constraint((t,), ea_day(day, time)))

                else:
                    if line[-1] in time_to_num:
                        time = time_to_num[line[-1]]
                        hard_constraint.append(Constraint((t,), ea_time(time)))

            if 'starts-in' in line:
                line_split = line[4].split('-')
                #print(line[3])
                day1 = week_to_num[line[3]]
                time1 = time_to_num[line_split[0]]
                day2 = week_to_num[line_split[1]]
                time2 = time_to_num[line[-1]]
                hard_constraint.append(Constraint((t,), si_day(day1,time1,day2,time2)))

            if 'ends-in' in line:
                line_split = line[4].split('-')
                #print(line)
                day1 = week_to_num[line[3]]
                time1 = time_to_num[line_split[0]]
                day2 = week_to_num[line_split[1]]
                time2 = time_to_num[line[-1]]
                hard_constraint.append(Constraint((t,), ei_day(day1, time1, day2, time2)))


        # gets all soft constraints
        if 'ends-by' in line:
            tasks = line[1]
            day = week_to_num[line[3]]
            time = time_to_num[line[4]]
            soft_cost[tasks] = int(line[-1])
            soft_constraint[tasks] = day * 10 + time

#print(task_domain)
#print(hard_constraint)
#print(soft_constraint)
#print(soft_cost)


csp = SOFT_CSP(task_domain, hard_constraint, soft_constraint, soft_cost)
problem = AC_CSP(csp)
solution = AStarSearcher(problem).search()

#print(solution)

if solution:
    solution = solution.end()
    for task in solution:
        for item in week_to_num:
            if week_to_num[item] == list(solution[task])[0][0] // 10:
                day = item
        for item in time_to_num:
            if time_to_num[item] == list(solution[task])[0][0] % 10:
                time = item
        print(f'{task}:{day} {time}')
    print(f'cost:{problem.heuristic(solution)}')
else:
    print('No solution')

