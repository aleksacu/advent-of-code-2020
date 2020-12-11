import os
import re


def execute_instruction(opcode, num, acc, pos):
    num = int(num)

    if opcode == "nop":
        pass
    elif opcode == "acc":
        acc += num
    elif opcode == "jmp":
        return acc, pos + num
    else:
        raise ValueError("Invalid instruction", opcode, num)

    return acc, pos + 1


def execute_instructions(instructions):
    acc = 0
    pos = 0
    executed = set()

    interrupted = False

    while True:
        if pos >= len(instructions):
            break

        opcode, num = instructions[pos]
        if (pos, opcode, num) in executed:
            interrupted = True
            break

        executed.add((pos, opcode, num))

        acc, pos = execute_instruction(opcode, num, acc, pos)

    return acc, executed, interrupted


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        instructions = f.read().splitlines()

    pattern = re.compile(r"(?P<opcode>[\w]+) (?P<num>[+-][0-9]+)")
    instructions = [re.match(pattern, i).groups() for i in instructions]

    acc, execd, _ = execute_instructions(instructions)

    print("Part one:", acc)

    for ins in execd:
        pos, opcode, num = ins
        if opcode in {"jmp", "nop"}:
            instructions[pos] = ("jmp" if opcode == "nop" else "nop", num)
            acc, _, interrupted = execute_instructions(instructions)
            if not interrupted:
                break
            instructions[pos] = (opcode, num)

    print("Part two:", acc)


if __name__ == "__main__":
    main()
