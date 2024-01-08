#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if their is a repetitive sequence in a linked list
 * @list: the linked list to check for repetitive sequence
 * Return: 1 if there exist a repetitive sequence
 * 0 if none exist
 */
int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;
	while (head != NULL)
	{
		head = head->next;
		if (head == list)
			return (1);
	}
	return (0);
}
