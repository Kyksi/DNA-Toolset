def color_output(seq: str) -> str:
    color_dict = {
        'A': '\033[1;34;48m',
        'C': '\033[1;31;48m',
        'G': '\033[1;32;48m',
        'T': '\033[1;33;48m',
        'U': '\033[1;33;48m',
        'reset': '\033[0;0m'
    }

    output = ''

    for nuc in seq:
        if nuc in color_dict:
            output += color_dict[nuc] + nuc
        else:
            output += color_dict['reset'] + nuc

    return output + color_dict['reset']
