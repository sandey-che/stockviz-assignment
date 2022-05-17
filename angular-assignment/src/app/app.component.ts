import { Component,OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'angular-assignment';
  public data: any;

  constructor(
    public http:HttpClient
  ) {}

ngOnInit(){
  console.log("extract data start")
  const url = "http://127.0.0.1:8000/GDP/?format=json"
  this.http.get(url).subscribe(res =>
    {
      this.data = res
      console.log(res)
      
    });

  }
}

