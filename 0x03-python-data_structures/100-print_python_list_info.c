#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info
 *	about python list
 * Return: void
 */

void print_python_list_info(PyObject *p);

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, p_Size;
	PyObject *p_Ind;
	PyTypeObject *p_Type;
	Py_ssize_t p_Alloc;
	
	char *p_Name;

	p_Type = Py_Type(p);
	p_Size = PyList_Size(p);
	p_Alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", p_Size);
	printf("[*] Allocated = %zd\n", p_Alloc);

	i = 0;
	while (i < p_Size)
	{
		p_Ind =  PyList_GetItem(p, i);

		p_Name = Py_TYPE(p_Ind)->tp_name;

		printf("Element %zd: %s\n", i, p_Name);
		i++;

	}
}
