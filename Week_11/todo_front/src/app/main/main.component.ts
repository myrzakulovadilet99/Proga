import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITasklist, ITask } from '../shared/models/model';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public task_lists: ITasklist[] = [];
  public loading = false;
  public name: any='';
  public tasks: ITask[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res=>{
      console.log('hjghgjh', res);
      this.task_lists = res;
      this.loading = true;
    });
  }

  getTasks(task_lists: ITasklist){
    this.provider.getTasks(task_lists).then(res=>{
      console.log(res);
      this.tasks = res;
    })
  }

  updateTaskList(tl: ITasklist){
    this.provider.updateTaskList(tl).then(res =>{
      console.log(tl.name+' updated');
    });
  }

  deleteTaskList(tl: ITasklist){
    this.provider.deleteTaskList(tl.id).then(res => {
      console.log(tl.name + 'deleted');
      this.provider.getTaskLists().then( res => {
        this.task_lists = res;
      })
    })
  }
  createTaskList(){
    if(this.name !== '') {
    this.provider.createTaskList(this.name).then( res => {
      this.name = '';
      this.task_lists.push(res);
      })
    }
}
}


