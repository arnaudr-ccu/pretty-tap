#!/usr/bin/env python3

# TAP pretty printer
# 

import re
import sys

import tap.parser


def pretty_tap(tap_text):

    ntests = 0
    nfails = 0
    output = []
    parser = tap.parser.Parser()

    lines = parser.parse_text(tap_text)
    if lines == []:
        return tap_text

    for line in lines:
        if line.category == 'test':
            ntests += 1
            if line.ok:
                if line.skip:
                    prefix = u' - '
                    # Unfortunately we must hack around to get a proper text here...
                    # (this might break with different versions of bats or python3-tap)
                    text = ''
                    if line.directive and line.directive.text:
                        text = line.directive.text
                    if text:
                        m = re.match("^skip \((.*)\) (.*)", text)
                        if m:
                            g = m.groups()
                            if g and len(g) == 2:
                                text = "{} (skipped: {})".format(g[1], g[0])
                else:
                    prefix = u' \N{check mark} '
                    text = line.description
            else:
                nfails += 1
                prefix = u' \N{ballot x} '
                text = line.description
            output.append(u"" + prefix + text)

        elif line.category == 'diagnostic':
            output.append(u"   " + line.text)

    output.append(u"")
    output.append(u"" + str(ntests) + " test(s), " + str(nfails) + " failure(s)")

    return "\n".join(output)


def main(argv=sys.argv, stream=sys.stderr):

    if len(sys.argv) == 1:
        buf = sys.stdin.read()
    elif len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as fd:
            buf = fd.read()
    else:
        print("Usage: {} [FILE.tap]".format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    #print(buf)

    buf = pretty_tap(buf)
    print(buf)



if __name__ == '__main__':
    main()
