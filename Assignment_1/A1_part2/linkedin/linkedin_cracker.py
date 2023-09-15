import hashlib


def get_pw_dict(pw_fn):

    """
    takes input file path, outputs raw_pws_dict where key = SHA1 hashed
    password from file value = plain text password
    """

    raw_pws_dict = dict()

    with open(pw_fn, 'r') as pw_file:
        pws = pw_file.readlines()
        for pw in pws:
            hashed_pw = hashlib.sha1(bytes(pw.strip(), 'UTF-8')).hexdigest()
            raw_pws_dict[hashed_pw] = pw.strip()

    return raw_pws_dict


def check_linkedin_pws(linkedin_file, raw_pws_dict):

    """
    takes linkedin pw file and raw_pws_dict from get_pw_dict, checks
    linkedin passwords against hashed passwords in raw_pws_dict.
    Outputs list of matching passwords where each element is formatted
    as '<hashed pw> <plain text pw>'
    """

    result = list()

    with open(linkedin_file, 'r') as pw_file:
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
    pw_file = 'Assignment_1/A1_part2/guesses.txt'
    linkedin_file = 'Assignment_1/A1_part2/linkedin/SHA1.txt'
    outfile = 'Assignment_1/A1_part2/linkedin/linkedin_submission.txt'

    raw_pws_dict = get_pw_dict(pw_file)
    result = check_linkedin_pws(linkedin_file, raw_pws_dict)
    print_to_file(outfile, result)


if __name__ == '__main__':
    main()
