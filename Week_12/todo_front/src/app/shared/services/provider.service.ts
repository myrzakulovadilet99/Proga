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

}
