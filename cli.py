import argparse
import asyncio
import json
from services import create_task_logic, _update_task, delete_task_logic, _list_task

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='taskmaster project')
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')

        create_parser = subparsers.add_parser('add', help='Create a new task')
        create_parser.add_argument('description', type=str, help='Task description')

        task_update_parser = subparsers.add_parser('update', help='Update a listed task')
        task_update_parser.add_argument('id', type=int, help='Task ID')
        task_update_parser.add_argument('description', type=str, help='Task description')

        mark_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task as in-progress')
        mark_progress_parser.add_argument('id', type=int, help='Task ID')

        mark_done_parser = subparsers.add_parser('mark-done', help='Mark task as done')
        mark_done_parser.add_argument('id', type=int, help='Task ID')

        delete_parser = subparsers.add_parser('delete', help='Delete a listed task')
        delete_parser.add_argument('id', type=int, help='Task ID')

        get_parser = subparsers.add_parser('list', help='Get a list of tasks')
        get_parser.add_argument('status', type=str, nargs='?', default=None, help='Task status')

        args = parser.parse_args()
        
        result = None

        if args.command == 'add':
            result = asyncio.run(create_task_logic(args.description))
        elif args.command == 'update':
            result = asyncio.run(_update_task(args.id, new_task=args.description))
        elif args.command == 'mark-in-progress':
            result = asyncio.run(_update_task(args.id, status="in-progress"))
        elif args.command == 'mark-done':
            result = asyncio.run(_update_task(args.id, status="done"))
        elif args.command == 'delete':
            result = asyncio.run(delete_task_logic(args.id))
        elif args.command == 'list':
            result = asyncio.run(_list_task(status=args.status))
        else:
            print("Invalid argument!")
            exit(1)

        if result:
            print(json.dumps(result, indent=2))
    except KeyboardInterrupt:
        print("\nExiting")