import hashlib


def get_pw_dict(pw_fn):

    """
    takes input file path, outputs raw_pws_dict where key = salted SHA256
    hashed password from file, value = plain text password
    """

    raw_pws_dict = dict()

    with open(pw_fn, 'r') as pw_file:
        pws = pw_file.readlines()
        for pw in pws:
            for salt in range(0, 100):
                salt = str(salt)
                hashed_pw = hashlib.sha256(bytes(salt, 'UTF-8')
                                           + bytes(pw.strip(), 'UTF-8'))
                raw_pws_dict[hashed_pw.hexdigest()] = pw.strip()

    return raw_pws_dict


def check_linkedin_pws(formspring_file, raw_pws_dict):

    """
    takes formspring pw file and raw_pws_dict from get_pw_dict, checks
    formspring passwords against hashed passwords in raw_pws_dict.
    Outputs list of matching passwords where each element is formatted
    as '<salted hashed pw> <plain text pw>'
    """

    result = list()

    with open(formspring_file, 'r') as pw_file:
        lines = pw_file.readlines()
        for line in lines:
            if line.strip() in raw_pws_dict:
                result.append(line.strip() + ' ' + raw_pws_dict[line.strip()])
                continue

    return result


def print_to_file(out_fn, pw_list):

    """
    takes an output file name and a list of passwords, writes the list
    to the output file
    """

    with open(out_fn, 'w') as outfile:
        for pw in pw_list[:100]:  # limit submission to 100 lines
            outfile.write(pw + '\n')


def main():
    guesses_file = 'Assignment_1/A1_part2/guesses.txt'
    formspring_file = 'Assignment_1/A1_part2/formspring/formspring.txt'
    outfile = 'Assignment_1/A1_part2/formspring/formspring_submission.txt'

    raw_pws_dict = get_pw_dict(guesses_file)
    result = check_linkedin_pws(formspring_file, raw_pws_dict)
    print_to_file(outfile, result)


if __name__ == '__main__':
    main()
