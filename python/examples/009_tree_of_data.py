"""Пример построения древовидной структуры данных"""


import re


class Branch:
    def __init__(self, parent):
        self.parentNode = parent
        self.nodes = []
        self.offset = ''
        self.offset_value = " "
        self.after_value = '---+'
        self.size = 1

    def close_branch(self):
        for node in self.nodes:
            if len(node.value) > self.size:
                self.size = len(node.value)
        for node in self.nodes:
            if node.childBranch:
                node.childBranch.offset = self.offset_value * (self.size +3)
                if node != self.nodes[-1]:
                    node.childBranch.offset = "|" + node.childBranch.offset[1:]

    def __str__(self):
        result = ""
        for node in self.nodes:
            result += str(node) + "\n"
            if node.childBranch:
                result += str(node.childBranch)
        return result

    def get_offset(self):
        result = ''
        if self.parentNode:
            result += self.parentNode.branch.get_offset()
        result += self.offset
        return result


class Node:
    def __init__(self, branch, value):
        self.branch = branch
        self.value = value
        self.childBranch = None
        self.after = ''

    def __str__(self):
        if self.childBranch:
            self.after = "-" * (self.branch.size - len(self.value)) + self.branch.after_value
        return f"{self.branch.get_offset()}{self.value}{self.after}"


class Tree:
    def __init__(self, string):
        self.branches = []
        self.work_branch = None
        for commands in string.split():
            self.exe_commands(commands)

    def exe_commands(self, commands):
        for command in re.search(r'(\(?)(\d+)(\)*)', commands).groups():
            if command == "":
                continue
            if command == "(":
                branch = Branch(None) if not self.work_branch else Branch(self.work_branch.nodes[-1])
                if not self.work_branch:
                    self.branches.append(branch)
                else:
                    self.work_branch.nodes[-1].childBranch = branch
                self.work_branch = branch
            if ")" in command:
                for i in command:
                    self.work_branch.close_branch()
                    if self.work_branch.parentNode:
                        self.work_branch = self.work_branch.parentNode.branch
                    else:
                        self.work_branch = None
            if command.isdigit():
                node = Node(self.work_branch, command)
                self.work_branch.nodes.append(node)

    def __str__(self):
        result = ""
        for branch in self.branches:
            result += str(branch) + "\n"
        return result


datas = [
         '(75 5 (23 3) 4)',
         '(4 5 6 (7) 108 (9)) (5 (6 7) 345)',
         '(43422 (233 22 233 (233 34 (45) 23 33)) 5 6 (72 244 2) 108 (9 (233 23 24)) 2) (5 (6 7) 345)',
         ]

for data in datas:
    tree = Tree(data)
    print("-" * 40)
    print(tree)
