#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_list - A function to print cpython list
 * @p: onject's llist to be printed
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long i;
	long length = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < length; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - A function to print python bytes
 * @p: objects byte to print
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *bytes;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);
	printf("[*] Python bytes info\n");
	printf("[*] Size: %zd\n", size);
	printf("first %zd bytes: ", size < 10 ? size : 10);
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)bytes[i]);
	}
	printf("\n");
}
