#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 *  main - entry point.
 *
 *  Return: 0 if successful or NULL if failure.
 */

int main(void)
{
	PyObject *obj1 = Py_BuildValue("[s#]", "Hello, Python!", 13);
	PyObject *obj2 = PyFloat_FromDouble(3.14159);
	PyObject *obj3 = PyBytes_FromStringAndSize("OpenAI GPT-3.5", 15);
	
	printf("[*] Calling print_python_list(obj1)\n");
	print_python_list(obj1);
	
	printf("\n[*] Calling print_python_float(obj2)\n");
	print_python_float(obj2);
	
	printf("\n[*] Calling print_python_bytes(obj3)\n");
	print_python_bytes(obj3);
	
	Py_XDECREF(obj1);
	Py_XDECREF(obj2);
	Py_XDECREF(obj3);
	
	return (0);
}

#endif
