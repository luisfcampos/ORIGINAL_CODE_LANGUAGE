import os.path as Path

# Project 3
# Author: Tyler Phan, Omar Ahmed, Luis Campos


# int_to_hex: convert an decimal (int) to hex (string)
# Input: x = input integer (int)
# Return: hex (string)
def int_to_hex(x):
    if (x < 0):
        x = neg_int_to_hex(x)
    else:
        x = "0x" + str(hex(x))[2:].zfill(2)

    return x

# neg_int_to_hex:
# Input: x = input integer (int)
# Return: x = 2's complemented hexadecimal (string)
def neg_int_to_hex(x):
    x = bin(x & 0xff)[2:]
    x = hex(int(x, 2))[2:].zfill(2)
    x = "0x" + x

    return x

# output statistics
def outputStatistics(total, alu, jump, branch, memory, other):
  print("Instruction Statistics \n")
  output_file.write("\n\nInstruction Statistics" + "\n")

  titles = ["ALU:", "Jump:", "Branch:", "Memory:", "Other:", "Total:"]
  vals = [alu, jump, branch, memory, other, total]

  i=0
  while i < len(titles):
    print(f"{titles[i]:<8}{vals[i]:<8}")
    output_file.write(f"{titles[i]:<8}{vals[i]:<8}" + "\n")
    i += 1

# output register final results and final PC result
def outputRegisters(reg, pc):
    hexValue = 0
    pReg = "Register"
    pVal = "Value"
    print(f"{pReg:<15}{pVal:^12}")

    # output header output file
    row_item = [pReg, pVal]
    output = '{:<15}{:^12}'.format(row_item[0], row_item[1])
    output_file.write(output + "\n")

    # output 32 registers from reg array
    for i in range(len(reg)):
        pReg = "$" + str(i)
        if (hexValue == 0):
            pVal = str(reg[i])
        else:
            pVal = int_to_hex(reg[i])
        print(f"{pReg:<15}{pVal:>12}")

        # output to txt file
        row_item = [pReg, pVal]
        output = '{:<15}{:>12}'.format(row_item[0], row_item[1])
        output_file.write(output + "\n")

    # output special registers
    pReg = "pc"
    if (hexValue == 0):
        pVal = str(pc)
    else:
        pVal = int_to_hex(pc)

    print(f"{pReg:<15}{pVal:>12}")

    row_item = [pReg, pVal]  # output to txt file
    output = '{:<15}{:>12}'.format(row_item[0], row_item[1])
    output_file.write(output + "\n")

    print("\n")
    print("\n")

# output data memory with values in HEX
def outputDM(mem):
    addr = v1 = v2 = v3 = v4 = v5 = v6 = v7 = v8 = ""
    addr = "Address"
    v1 = "Value (+0)"
    v2 = "Value (+1)"
    v3 = "Value (+2)"
    v4 = "Value (+3)"
    v5 = "Value (+4)"
    v6 = "Value (+5)"
    v7 = "Value (+6)"
    v8 = "Value (+7)"
    row_item = [addr, v1, v2, v3, v4, v5, v6, v7, v8]
    output = '|{:>10}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|'.format(
        row_item[0], row_item[1], row_item[2], row_item[3], row_item[4],
        row_item[5], row_item[6], row_item[7], row_item[8])
    output_file.write("\n" + output + "\n")
    print(
        f"|{addr:>15}|{v1:>15}|{v2:>15}|{v3:>15}|{v4:>15}|{v5:>15}|{v6:>15}|{v7:>15}|{v8:>15}|"
    )
    j = 0
    for i in range(32):
        addr = str(i * 8)
        if j < len(mem):
            if mem[j] < 0:
                v1 = neg_int_to_hex(mem[j]).zfill(2)
            else:
                v1 = str(hex(mem[j]).zfill(2))
        if (j + 1) < len(mem):
            if mem[j + 1] < 0:
                v2 = neg_int_to_hex(mem[j + 1]).zfill(2)
            else:
                v2 = str(hex(mem[j + 1]).zfill(2))
        if (j + 2) < len(mem):
            if mem[j + 2] < 0:
                v3 = neg_int_to_hex(mem[j + 2]).zfill(2)
            else:
                v3 = str(hex(mem[j + 2]).zfill(2))
        if (j + 3) < len(mem):
            if mem[j + 3] < 0:
                v4 = neg_int_to_hex(mem[j + 3]).zfill(2)
            else:
                v4 = str(hex(mem[j + 3]).zfill(2))
        if (j + 4) < len(mem):
            if mem[j + 4] < 0:
                v5 = neg_int_to_hex(mem[j + 4]).zfill(2)
            else:
                v5 = str(hex(mem[j + 4]))
        if (j + 5) < len(mem):
            if mem[j + 5] < 0:
                v6 = neg_int_to_hex(mem[j + 5]).zfill(2)
            else:
                v6 = str(hex(mem[j + 5]).zfill(2))
        if (j + 6) < len(mem):
            if mem[j + 6] < 0:
                v7 = neg_int_to_hex(mem[j + 6]).zfill(2)
            else:
                v7 = str(hex(mem[j + 6]).zfill(2))
        if (j + 7) < len(mem):
            if mem[j + 7] < 0:
                v8 = neg_int_to_hex(mem[j + 7]).zfill(2)
            else:
                v8 = str(hex(mem[j + 7]).zfill(2))
        print(
            f"|{addr:>15}|{v1:>15}|{v2:>15}|{v3:>15}|{v4:>15}|{v5:>15}|{v6:>15}|{v7:>15}|{v8:>15}|"
        )
        row_item = [addr, v1, v2, v3, v4, v5, v6, v7, v8]
        output = '|{:>10}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|{:>15}|'.format(
            row_item[0], row_item[1], row_item[2], row_item[3], row_item[4],
            row_item[5], row_item[6], row_item[7], row_item[8])
        output_file.write(output + "\n")
        j += 8
    print("\n")

# take in binary string and return twos comp of the string
def twosComp(s):
    for j in reversed(range(len(s))):
        if s[j] == '1':
            break

    t = ""
    for i in range(0, j, 1):  # flip everything
        t += str(1 - int(s[i]))

    for i in range(j, len(s), 1):  # until the first 1 from the right
        t += s[i]

    return t  # return 2's complement binary (string)

# returns two's comp integer value
def twoscomp_dec(b):

    l = len(b)  # length of bit provided

    x = b[:1].zfill(
        l)  # save the first bit and fill with 0's until original length
    x = x[::-1]  # flip binary

    x = int(x, 2) * -1  # value of binary (unsigned: 10000..0) * -1

    y = int(b[1:], 2)  # value of binary without the first bit

    x += y  # add up differing values

    return x  # return 2's complement decimal (int)


# itosbin: convert integer (int) to signed binary (string)
# Input: i = integer (int) | n = # of bits of desired binary
# Return: returns signed binary (string)
def itosbin(i, n):
    s = ""
    if i >= 0:
        s = bin(i)[2:].zfill(n)
    else:
        s = bin(0 - i)[2:].zfill(n)
        s = twosComp(s)
    return s

# binary to decimal
# init parameter used to determine if value should be signed or unsigned
def bin_to_dec(b, init):
    if (b[0] == "0" or init == "1"):
        return int(b, base=2)
    else:
        return twoscomp_dec(b)

# convert hex to 8 bit binary 
def hex_to_bin(line):
    h = line.replace("\n", "")
    i = int(h, base=16)
    b = bin(i)
    b = b[2:].zfill(8)
    return (b)

# process binary machine code
# returns instruction
def process(b):
    b_op = b[0:3]
    b_op1 = b[0:2]
    b_func = b[3]
    b_func2 = b[4]
    asm = ""

    if (b_op == "000"):
        if (b_func == "0"):  #ld
            rx = int(b[4:7], base=2)
            ry = int(b[7], base=2)
            rx = str(rx)
            ry = str(ry)
            instr = "ld"
        elif (b_func == "1"):  #st
            rx = int(b[4:7], base=2)
            ry = int(b[7], base=2)
            rx = str(rx)
            ry = str(ry)
            instr = "st"
        asm = instr + " $" + rx + " $" + ry
        #print(f'in asm: {asm}')

    elif (b_op == "001"):
        rx = int(b[4:6], base=2)
        ry = int(b[6:], base=2)
        rx = str(rx)
        ry = str(ry)
        if (b_func == "0"):  #slt
            instr = "sltR7"
        elif (b_func == "1"):  #xor
            instr = "xor"

        asm = instr + " $" + rx + " $" + ry
        #print(f'in asm: {asm}')

    elif (b_op == "010"):
        rx = int(b[5:8], base=2)
        if (b_func == "0"):
            if (b_func2 == "0"):  # srl
                instr = "srl"
                rx = str(rx)
            elif (b_func2 == "1"):  # and
                instr = "and"
                rx = str(rx)
            asm = instr + " $" + rx
            #print(f'in asm: {asm}')
        elif (b_func == "1"):  # j
            imm = b[4:8]
            instr = "j"
            immS = bin_to_dec(imm, "0")
            immS = str(immS)
            asm = instr + " " + immS
            #print(f'in asm: {asm}')

    elif (b_op == "011"):  # add
        rx = int(b[3:5], base=2)
        ry = int(b[5:8], base=2)
        instr = "add"
        rx = str(rx)
        ry = str(ry)
        asm = instr + " $" + rx + ", $" + ry
        #print(f'in asm: {asm}')

    elif (b_op == "100"):  # sub
        rx = int(b[3:6], base=2)
        ry = int(b[6:8], base=2)
        instr = "sub"
        rx = str(rx)
        ry = str(ry)
        asm = instr + " $" + rx + ", $" + ry
        #print(f'in asm: {asm}')

    elif (b_op == "101"):  # bez
        rx = int(b[3:5], base=2)
        imm = b[5:]
        instr = "bez"
        rx = str(rx)
        immS = bin_to_dec(imm, "0")
        immS = str(immS)
        asm = instr + " $" + rx + ", " + immS
        #print(f'in asm: {asm}')

    elif (b_op == "110"):  # addi
        rx = int(b[3:6], base=2)
        imm = b[6:]
        instr = "addi"
        rx = str(rx)
        immS = bin_to_dec(imm, "0")
        immS = str(immS)
        asm = instr + " $" + rx + ", " + immS
        #print(f'in asm: {asm}')

    elif (b_op == "111"):
        if (b_func == "1"):
            imm = b[4:8]
            instr = "init"
            immS = bin_to_dec(imm, "1")
            immS = str(immS)
            asm = instr + " " + immS
            #print(f'in asm: {asm}')
        elif (b_func == "0"):
            instr = "halt"
            asm = instr
            #print(f'in asm: {asm}')
    return asm

# disassemble used to convert from instruction to binary
# input: instruction
# output: binary machine code
def disassemble(c):
    ld_1 = "ld"
    st_1 = "st"
    sltR0_1 = "sltR7"
    xorR0_1 = "xor"
    srl_1 = "srl"
    and_1 = "and"
    j_1 = "j"
    add_1 = "add"
    sub_1 = "sub"
    bez_1 = "bez"
    addi_1 = "addi"
    init_1 = "init"
    halt_1 = "halt"

    bin_out = ''
    if init_1 in c:  # init
        splitString = c.split()
        imm = itosbin(int(splitString[1]), 4)
        bin_out = bin_out + '1111' + imm
        return bin_out
    elif halt_1 in c:  # halt
        bin_out = bin_out + '11100000'
        return bin_out
    elif ld_1 in c:  # ld
        bin_out = bin_out + '0000'
        reg1 = bin(int(c.split('$')[1]))
        reg1 = reg1[2:].zfill(3)
        reg2 = bin(int(c.split('$')[2]))
        reg2 = reg2[2:]
        bin_out = bin_out + reg1 + reg2
    elif st_1 in c:  # st
        bin_out = bin_out + '0001'
        regs = c.split()
        reg1 = bin(int(regs[1][1]))
        reg1 = reg1[2:].zfill(3)
        reg2 = bin(int(regs[2][1]))
        reg2 = reg2[2:]
        bin_out = bin_out + reg1 + reg2
    elif sltR0_1 in c:  # slt
        bin_out = bin_out + '0010'
        regs = c.split()
        reg1 = bin(int(regs[1][1]))
        reg1 = reg1[2:].zfill(2)
        reg2 = bin(int(regs[2][1]))
        reg2 = reg2[2:].zfill(2)
        bin_out = bin_out + reg1 + reg2
    elif xorR0_1 in c:  # xor
        bin_out = bin_out + '0011'
        regs = c.split()
        reg1 = bin(int(regs[1][1]))
        reg1 = reg1[2:].zfill(2)
        reg2 = bin(int(regs[2][1]))
        reg2 = reg2[2:].zfill(2)
        bin_out = bin_out + reg1 + reg2
    elif srl_1 in c:  # srl
        bin_out = bin_out + '01000'
        reg1 = bin(int(c.split('$')[1]))
        reg1 = reg1[2:].zfill(3)
        bin_out = bin_out + reg1
    elif and_1 in c:  # and
        bin_out = bin_out + '01001'
        reg1 = bin(int(c.split('$')[1]))
        reg1 = reg1[2:].zfill(3)
        bin_out = bin_out + reg1
    elif j_1 in c:  # j
        bin_out = bin_out + '0101'
        imm = itosbin(int(c.split(' ')[1]), 4)
        bin_out = bin_out + imm
    elif c.split()[0] == add_1 in c:  # add
        bin_out = bin_out + '011'
        regs = c.split()
        reg1 = bin(int(regs[1][1]))
        reg1 = reg1[2:].zfill(2)
        reg2 = bin(int(regs[2][1]))
        reg2 = reg2[2:].zfill(3)
        bin_out = bin_out + reg1 + reg2
    elif sub_1 in c:  # sub
        bin_out = bin_out + '100'
        regs = c.split()
        reg1 = bin(int(regs[1][1]))
        reg1 = reg1[2:].zfill(3)
        reg2 = bin(int(regs[2][1]))
        reg2 = reg2[2:].zfill(2)
        bin_out = bin_out + reg1 + reg2
    elif bez_1 in c:  # bez
        bin_out = bin_out + '101'
        regs = c.split()
        reg1 = bin(int(regs[1][1]))
        reg1 = reg1[2].zfill(2)
        imm = bin(int(regs[2]))
        imm = imm[2:].zfill(3)
        bin_out = bin_out + reg1 + imm
    elif c.split()[0] == addi_1 in c:  # addi
        bin_out = bin_out + '110'
        regs = c.split()
        reg1 = bin(int(regs[1][1]))
        reg1 = reg1[2:].zfill(3)
        imm = bin(int(regs[2]))
        if (int(regs[2]) < 0):  #imm is negative
            imm = itosbin(int(regs[2]), 2)
        else:
            imm = imm[2:].zfill(2)
        bin_out = bin_out + reg1 + imm

    return bin_out


# converts 8 bit machine code to instructions
def machineToInstructions(input_file, asmInstr):
    instr = []  # empty list of user inputs
    lineCount = 0

    for line in input_file:
        lineCount += 1
        bin_str = hex_to_bin(line)
        asmline = process(bin_str)
        output_file.write(asmline + '\n')
        asmInstr.append(asmline)
        asmline = asmline.replace("j", "j,")  # remove j and replace w/ "j,"
        asmline = asmline.replace("init",
                                  "init,")  # remove init and replace w/ "init,"
        asmline = asmline.replace(", $",
                                  ",")  # remove middle $ and replace w/ ","
        asmline = asmline.replace(" $",
                                  ",")  # remove first $ and replace w/ ","
        asmline = asmline.replace(" ", "")  # remove extra spacing
        asmline = asmline.split(",")  # split by "," and generate a list
        instr.append(asmline)

    output_file.write("\n")  # newline in output file to show finished
    input_file.close()  # close input file since we no longer need it

    return instr  # return list of listed instructions


#srl bit shifted by 1
# b is binary string
def srl(b):
    r = 7
    b = b[0:r].zfill(8)

    return bin_to_dec(b, "0")


# b is binary string
# and 1
def and1(b):
    s = ""
    if b[7] == '1':
        s += '1'
    else:
        s += '0'

    return s.zfill(8)

# 8 bit XOR operation
# input: 2 8-bit strings
# output: returns decimal value
def xor(b1, b2):
    s = ""
    for i in range(8):
      if (b1[i] == "0" and b2[i] == "1") or (b1[i] == "1" and b2[i] == "0"):
       s += "1"
      else:
       s += "0"
    return bin_to_dec(s,"0")

# --------------------- MAIN ----------------------------------
x = ""
input_o = ""
while x != "1" or x != "2" or x != "3": # prompt which file to run
  x = input("Enter 1, 2, or 3 for awv1, awv2, or toy>")
  if x == "1":
    input_o = "awv1"
    input_file = "awv1.txt"
    break;
  elif x == "2":
    input_o = "awv2"
    input_file = "awv2.txt"
    break;
  elif x == "3":
    input_o = "toy"
    input_file = "toy.txt"
    break;

file_exists = 0
while (file_exists != 1):
  if Path.isfile(input_file): # file exists
    print("File sucessfully loaded")
    input_file = open(input_file, "r")              # open input file in read mode (r)
    file_exists = 1                                 # file exists so set true
  else: # file does not exist, so ask for valid file
    print("File does not exist")
    file_exists = 0                                 # file does not exists so set false
    input_file = input("Enter input file> ")
output_file = input_o + "_output.txt"
output_file = open(output_file,"w")
#instr holds deconstructed instructions
instr = []
pInstr = []
asmInstr = []
instr = machineToInstructions(input_file, asmInstr)

# 8 registers
reg = [0] * 8
# DM
mem = [0] * 256
pc = line = 0


cLine = "line"
cInstruction = "Intruction"
cResult = "Result"
cPC = "PC"

print(f"{cLine:<15}{cInstruction:<35}{cResult:<25}{cPC:<15}")
cRow = [cLine, cInstruction, cResult, cPC]
output = '{:<8}{:<24}{:<26}{:<8}'.format(cRow[0], cRow[1], cRow[2], cRow[3])

output_file.write(output + "\n")

total = alu = jump = branch = memory = other = 0

#loop through IM
while (pc < len(instr)):
    cur = instr[pc] # cur = ["instr", "$x", "$y/imm"]
    line += 1
    # cur[] = [bez, 1, imm]
    if (cur[0] == 'j' or cur[0] == "bez"):
        if cur[0] == 'j':
            cInstruction = asmInstr[pc]
            pc += 1 + int(cur[1])
            cResult = "jump to PC " + str(pc)
            jump += 1
        else: #branch equal 0
            if (reg[int(cur[1])] == 0):
                cInstruction = asmInstr[pc]
                pc += 1 + int(cur[2])
                cResult = "branch to PC " + str(pc)
            else:
                cInstruction = asmInstr[pc]
                pc += 1
                cResult = "No branch"
            branch += 1

    elif (cur[0] == "ld" or cur[0] == "st"):
        if cur[0] == "ld":
            cInstruction = asmInstr[pc]
            reg[int(cur[1])] = mem[reg[int(cur[2])]]
            cResult = "$" + cur[1] + " = " + str(reg[int(cur[1])])
        else:
            #print(pc)
            cInstruction = asmInstr[pc]
            mem[reg[int(cur[2])]] = reg[int(cur[1])]
            cResult = "DM[" + str(reg[int(cur[2])]) + "] = " + str(reg[int(cur[1])])
        pc += 1
        memory += 1

    else:
        if cur[0] == "addi":
            reg[int(cur[1])] = int(reg[int(cur[1])]) + int(cur[2])
            cInstruction = asmInstr[pc]
            cResult = "$" + cur[1] + " = " + str(reg[int(cur[1])]) 
            
        elif cur[0] == "init":
            reg[0] = int(cur[1])
            cInstruction = asmInstr[pc]
            cResult = "$0 = " + cur[1]
        elif cur[0] == "halt":
            break
        elif cur[0] == "add":
            reg[int(cur[1])] = reg[int(cur[1])] + reg[int(cur[2])]
            cInstruction= asmInstr[pc]
            cResult = "$" + cur[1] + " = " + str(reg[int(cur[1])]) 
        elif cur[0] == "sub":
            reg[int(cur[1])] = reg[int(cur[1])] - reg[int(cur[2])]
            cInstruction = asmInstr[pc]
            cResult = "$" + cur[1] + " = " + str(reg[int(cur[1])]) 
        elif cur[0] == "sltR7":
            if int(reg[int(cur[1])]) < int(reg[int(cur[2])]):
                reg[7] = 1
                cInstruction = asmInstr[pc]
                cResult = "$7" + " = " + "1"
            else:
                reg[7] = 0
                cInstruction = asmInstr[pc]
                cResult = "$7" + " = " + "0"
            other += 1
        elif cur[0] == "srl":
            reg[int(cur[1])] = int(srl(itosbin(reg[int(cur[1])], 8)))
            cInstruction = asmInstr[pc]
            cResult = "$" + cur[1] + " = " + str(reg[int(cur[1])]) 
        elif cur[0] == "xor":
            x = itosbin(reg[int(cur[1])],8)
            y = itosbin(reg[int(cur[2])],8)
            reg[int(cur[1])] = xor(x, y)
            cInstruction = asmInstr[pc]
            cResult = "$" + cur[1] + " = " + str(reg[int(cur[1])]) 
        elif cur[0] == "and":
            reg[int(cur[1])] = int(and1(itosbin(reg[int(cur[1])], 8)))
            cInstruction = asmInstr[pc]
            cResult = "$" + cur[1] + " = " + str(reg[int(cur[1])]) 
        alu += 1
        pc += 1
    pInstr.append(cur)
    cPC = pc
    cLine = line
    print(f"{cLine:<15}{cInstruction:<35}{cResult:<25}{cPC:<15}")
    cRow = [cLine, cInstruction, cResult, cPC]
    output = '{:<8}{:<24}{:<26}{:<8}'.format(cRow[0], cRow[1], cRow[2], cRow[3])
    output_file.write(output + "\n")
    print(cur)
    
output_file.write("\n")
total = alu + jump + branch + memory + other
outputRegisters(reg, pc)
outputDM(mem)
outputStatistics(total, alu, jump, branch, memory, other)

input_file.close()
output_file.close()

# end of main
# ---------------------------------------------------------------- #

# below used to convert from instruction to 8 bit binary to hex

# disassembler 
# input_file = open("asm_in.txt", "r")
# output_file = open("binary_out.txt", "w")
# line_count = 0

# for line in input_file:
#     line_count += 1
#     bin_str = str(line)
#     asmline = disassemble(bin_str)
#     output_file.write(asmline + '\n')

# input_file.close()
# output_file.close()

# input_file = open("binary_out.txt", "r")
# output_file = open("HEXINSTR.txt", "w")
# line_count = 0

# for line in input_file:
#     line_count += 1
#     bin_str = str(line)
#     asmline = hex(int(line, 2))
#     output_file.write(asmline[2:].zfill(2) + '\n')

# input_file.close()
# output_file.close()
