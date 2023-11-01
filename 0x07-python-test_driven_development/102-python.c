#include "python_string_printer.h"
#include <Python.h>

/**
 * print_python_string - Print information about a Python string object.
 *
 * This function checks if the provided object is a valid Python string and
 * prints information about the string, including its type, length, and value.
 *
 * @p: A pointer to a Python object to be printed.
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	Py_UNICODE *unicode_str;

	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "c a" : "c u o");
		length = PyUnicode_GET_LENGTH(p);
		unicode_str = PyUnicode_AS_UNICODE(p);
		printf("  length: %zd\n", length);
		printf("  value: %ls\n", unicode_str);
	} else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
