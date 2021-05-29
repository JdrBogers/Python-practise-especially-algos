# python3
import numpy
                                    
def LCS3(s1, s2, s3, n1, n2, n3):


if __name__ == '__main__':
    n1, s1, n2, s2, n3, s3 = int(input()), input(), int(input()), input(), int(input()), input()
    
    LCS_length, Matrix = LCS3(s1, s2, s3, n1, n2, n3)
    print('Length of LCS:', LCS_length)
    sequence = printSubsequence(Matrix, s1, s2, s3, n1, n2, n3, [])
    print('LCS:', sequence)