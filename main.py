'''
Main module with arch-important logic
'''
import tools
import debug

if __name__ == '__main__':
    args = tools.parse_args()

    if args.mode == 'debug':
        debug.debug()
    elif args.mode == 'release':
        pass
