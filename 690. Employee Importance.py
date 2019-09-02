"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        save = {}
        for i in range(len(employees)):
            save[employees[i].id] = (employees[i].importance, employees[i].subordinates)

        def deep(idnum, val):
            if len(save.get(idnum)[1]) == 0:
                return save.get(idnum)[0]
            else:
                cur = save.get(idnum)[0]
                for num in save.get(idnum)[1]:
                    cur = cur + deep(num, cur)
                return cur

        return deep(id, 0)



