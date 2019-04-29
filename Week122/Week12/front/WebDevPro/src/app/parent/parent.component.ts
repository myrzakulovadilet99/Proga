import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ICategory, IProduct} from '../shared/models/models';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.scss']
})
export class ParentComponent implements OnInit {

  public output = '';
  public stringArray: string[] = [];

  public categories: ICategory[] = [];
  public loading = false;

  public products: IProduct[] = [];

  public name: any = '';

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {

    this.provider.getCategories().then(res => {
      this.categories = res;
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });
  }

  getProducts(category: ICategory) {
    this.provider.getProducts(category).then(res => {
      this.products = res;
    });
  }

  sendMessageByService() {
    this.provider.sendMessage.emit('This message From Parent Component');
  }

  updateCategory(c: ICategory) {
    this.provider.updateCategory(c).then(res => {
      console.log(c.name + ' updated');
    });
  }

  deleteCategory(c: ICategory) {
    this.provider.deleteCategory(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getCategories().then(r => {
        this.categories = r;
      });
    });
  }

  createCategory() {
    if (this.name !== '') {
      this.provider.createCategory(this.name).then(res => {
        this.name = '';
        this.categories.push(res);
      });
    }
  }

}
