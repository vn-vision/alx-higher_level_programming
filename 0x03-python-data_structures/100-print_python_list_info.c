#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info
 *	about python list
 * Return: void
 */
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid argument: Not a Python list\n");
        return;
    }

    Py_ssize_t i, size = PyList_GET_SIZE(p);
    PyListObject *obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", obj->allocated);

    for (i = 0; i < size; i++)
        printf("Element %zd: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}

