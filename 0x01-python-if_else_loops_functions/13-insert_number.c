#include <stdlib.h>
#include "lists.h"
#include <stdio.h>
/**
 * insert_node - function to insert a number into a  singly linked list
 * @head: head node
 * @number: new node.
 * Return: address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *new_node = NULL, *x = NULL, *z = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number, new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	x = *head;
	if (number <= x->n)
	{
		new_node->next = x, *head = new_node;
		return (*head);
	}
	if (number > x->n && !x->next)
	{
		x->next = new_node;
		return (new_node);
	}
	z = x->next;
	while (x)
	{
		if (!z)
			x->next = new_node, flag = 1;
		else if (z->n == number)
			x->next = new_node, new_node->next = z, flag = 1;
		else if (z->n > number && actual->n < number)
			x->next = new_node, new_node->next = z, flag = 1;
		if (flag)
			break;
		x = x->next, x = x->next;
	}
	return (new_node);
}
