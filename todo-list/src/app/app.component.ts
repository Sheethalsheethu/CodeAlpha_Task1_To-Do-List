import { Component } from '@angular/core';

interface TodoItem {
  task: string;
  completed: boolean;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  todoList: TodoItem[] = [];
  newTask: string = '';

  addTask() {
    if (this.newTask.trim() !== '') {
      this.todoList.push({ task: this.newTask, completed: false });
      this.newTask = '';
    }
  }

  completeTask(index: number) {
    this.todoList[index].completed = true;
  }

  deleteTask(index: number) {
    this.todoList.splice(index, 1);
  }
}
