if __name__ == '__main__':
    with open('INPUT.TXT', 'r') as input_file, open('OUTPUT.TXT', 'w') as output_file:
        a, b = map(int, input_file.read().split())
        print(a + b, file=output_file)