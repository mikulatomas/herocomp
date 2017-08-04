def filename_directive(filename):
    return "\t.file\t\"{0}\"\n".format(filename)


def compiler_ident_directive():
    return "\t.ident\t\"{0}\"\n".format("HEROCOMP - Tomas Mikula 2017")


def text_directive():
    return "\t.text\n"


def data_directive():
    return "\t.data\n"


def quad_directive(arg):
    return "\t.quad\t{}\n".format(arg)


def global_array(identifier, size):
    return "\t.comm {0},{1},32\n".format(identifier, size * 8)


def global_directive(arg):
    return "\t.global\t{0}\n".format(arg)


def label(name):
    return "{0}:\n".format(name)


def instruction(name, *args):
    code = "\t{0}\t".format(name)

    for i in range(len(args)):
        if i == len(args) - 1:
            code += "{0}".format(args[i])
        else:
            code += "{0}, ".format(args[i])

    code += "\n"

    return code


def number_constant(number):
    return "${0}".format(number)
