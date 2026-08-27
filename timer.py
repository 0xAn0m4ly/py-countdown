import time
import argparse

def timer(input_time):
    for i in range(input_time):
        input_time -= 1
        print(f'{input_time} ', end='\r')
        time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'A timer module...'
    )
    parser.add_argument('seconds', type=int, help='The argument must be an integer')
    args= parser.parse_args()
    timer(args.seconds)