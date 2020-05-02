#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlist_t listint.
 * @h: pointer to head
 * Return: i
 */
size_t print_dlistint(const dlistint_t *h)
{
	int i;
	const dlistint_t *aux = h;

	for (i = 0; aux != NULL; i++)
	{
		printf("%i\n", aux->n);
		aux = aux->next;
	}
	return (i);
}
