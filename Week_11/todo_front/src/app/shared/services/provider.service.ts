import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {ITasklist, ITask} from '../models/model';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITasklist[]> {
    return this.get('http://localhost:8000/api/task_lists/',{});
  }
  getTasks(taskList: ITasklist): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/task_lists/${taskList.id}/tasks`,{});
  }

  createTaskList(n: any): Promise<ITasklist> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: n
    });
  }

  updateTaskList(tasklist: ITasklist): Promise<ITasklist> {
    return this.put(`http://localhost:8000/api/task_lists/${tasklist.id}/`, {
      name: tasklist.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delete(`http://localhost:8000/api/task_lists/${id}/`, {});
  }
}


