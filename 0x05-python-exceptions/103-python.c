#!/usr/bin/python3
#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyObject *item;

    if (PyList_Check(p)) {
        size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++) {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
            if (PyBytes_Check(item)) {
                printf("[.] bytes object info\n");
                printf("  size: %ld\n", PyBytes_GET_SIZE(item));
                printf("  trying string: %s\n", PyBytes_AsString(item));
                printf("  first 10 bytes: ");
                for (Py_ssize_t j = 0; j < 10 && j < PyBytes_GET_SIZE(item); j++) {
                    printf("%02x ", PyBytes_AS_STRING(item)[j] & 0xFF);
                }
                printf("\n");
            }
        }
    } else {
        PyErr_Format(PyExc_TypeError, "Invalid List Object");
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size;
    PyObject *item;

    if (PyBytes_Check(p)) {
        size = PyBytes_GET_SIZE(p);
        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first 10 bytes: ");
        for (Py_ssize_t i = 0; i < 10 && i < size; i++) {
            printf("%02x ", PyBytes_AS_STRING(p)[i] & 0xFF);
        }
        printf("\n");
    } else {
        PyErr_Format(PyExc_TypeError, "Invalid Bytes Object");
    }
}

void print_python_float(PyObject *p) {
    if (PyFloat_Check(p)) {
        printf("[.] float object info\n");
        printf("  value: %lf\n", PyFloat_AsDouble(p));
    } else {
        PyErr_Format(PyExc_TypeError, "Invalid Float Object");
    }
}
