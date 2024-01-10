#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the pointer to a pointer to the list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list = *head, *temp = NULL, *new_node;
	int i = 0;

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;
	while (list != NULL)
	{
		if (i == 4)
		{
			temp = list->next;
			list->next = new_node;
			new_node->next = temp;
			break;
		}
		list = list->next;
		i++;
	}
	return (list);
}
