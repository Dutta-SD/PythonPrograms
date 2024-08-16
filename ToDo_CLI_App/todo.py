'''
-----------------------------------------------
todo : CLI tool for managing daily tasks
-----------------------------------------------
__author__ : Sandip Dutta
-----------------------------------------------
Note : Some error occuring due to help function
formatting issues
'''
### Required dependency, install via
### pip install click
import os
import sys
from datetime import datetime

# ------------ Dependencies--------------
import click


# ---------------------------------------


## Main init function of todo cli
@click.group()
def todo_cli():
    # init function for cli
    # args : None
    # return None
    pass


## Add function - adds the task to todo list
@todo_cli.command('add', help="$ add 'todo item' # Add a new todo")
@click.argument('todo_item', type=str, required=False)
def add(todo_item: str = None):
    # adds todo item to file (todo.txt) where we store 
    # tasks to be done

    if todo_item == None:
        click.echo("Error: Missing todo string. Nothing added!")
    with open('todo.txt', 'a') as todoDataFile:
        todoDataFile.write(f"{todo_item}\n")
        # Success confirmation
        click.echo(f"Added todo: \"{todo_item}\"")


## ls - Shows all the tasks remaining
@todo_cli.command('ls', help="$ ls # Show remaining todos")
def ls():
    # reports work done or not
    with open('todo.txt', 'r') as todoDataFile:
        todoTaskData = todoDataFile.readlines()
        numTasks = len(todoTaskData)
        if numTasks == 0:
            # no tasks
            click.echo('There are no pending todos!')
            sys.exit(0)

        # Print from reverse as per priority
        todoTaskData.reverse()
        for reversePriority, task in enumerate(todoTaskData):
            task = task.rstrip("\n")
            print(f"[{numTasks - reversePriority}] {task}")


# delete
@todo_cli.command('del', help='$ del NUMBER  # Delete a todo')
@click.argument('task_number', type=int, required=False)
def delete(task_number: int):
    # deletes a task
    # if not found, then raise error

    if task_number == None:
        click.echo(f'Error: Missing NUMBER for deleting todo.')
        sys.exit(0)

    with open('todo.txt', 'r+') as todoDataFile:
        todoTasks = todoDataFile.readlines()
        numTasks = len(todoTasks)
        if task_number > numTasks or task_number < 1:
            # invalid number
            errorMessage = f"Error: todo #{task_number} does not exist. Nothing deleted."
            click.echo(errorMessage)
            sys.exit(0)

        # valid, so remove item, clear file, write tasks again
        task = todoTasks[task_number - 1]
        todoTasks.remove(task)
        todoDataFile.truncate(0)
        todoDataFile.writelines(todoTasks)
        click.echo(f'Deleted todo #{task_number}')


@todo_cli.command('done', help='$ done NUMBER # Mark task as Done')
@click.argument('task_number', type=int, required=False)
def done(task_number):
    # marks task as done
    # if not found, then raise error
    task = None  ## task to be deleted

    if task_number == None:
        click.echo(f'Error: Missing NUMBER for marking todo as done.')
        sys.exit(0)

    with open('todo.txt', 'r+') as todoDataFile:
        todoTasks = todoDataFile.readlines()
        numTasks = len(todoTasks)
        if task_number > numTasks or task_number < 1:
            # invalid number
            errorMessage = f"Error: todo #{task_number} does not exist."
            click.echo(errorMessage)
            sys.exit(0)
        # valid, so remove item, clear file, write tasks again
        task = todoTasks[task_number - 1]
        todoTasks.remove(task)
        todoDataFile.truncate(0)
        todoDataFile.writelines(todoTasks)

    with open('done.txt', 'a') as doneTasks:
        # Current utc time
        task_complete_date = datetime.utcnow().strftime("%Y-%m-%d")
        ## Write task in final format
        doneTasks.write(f"x {task_complete_date} {task}")
        click.echo(f"Marked todo #{task_number} as done.")


@todo_cli.command('report', help='$ report # Statistics')
def report():
    ## Gives statistics for tasks
    pendingTasksData = open('todo.txt')
    completedTasksData = open('done.txt')

    numPendingTasks = len(pendingTasksData.readlines())
    numCompletedTasks = len(completedTasksData.readlines())

    dateNow = datetime.utcnow().strftime("%Y-%m-%d")

    tasksStatsToDisplay = f"{dateNow} Pending : {numPendingTasks} Completed : {numCompletedTasks}"
    click.echo(tasksStatsToDisplay)


@todo_cli.command('help', help="$ help # Show usage")
def give_help():
    # Shows help message
    help_text = '''Usage :-
    $ ./todo add \"todo item\"  # Add a new todo
    $ ./todo ls               # Show remaining todos
    $ ./todo del NUMBER       # Delete a todo
    $ ./todo done NUMBER      # Complete a todo
    $ ./todo help             # Show usage
    $ ./todo report           # Statistics'''
    click.echo(help_text)


if __name__ == '__main__':
    os.chdir('.')  # change to current dir
    ## Make necessary files
    todo_file = 'todo.txt'
    done_file = 'done.txt'
    ## Make files
    open(todo_file, 'a').close()
    open(done_file, 'a').close()
    # run cli
    todo_cli()
