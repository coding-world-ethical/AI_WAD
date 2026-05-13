import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './register.html',
  styleUrl: './register.css',
})

export class RegisterComponent {
  name = '';
  email = '';
  password = '';

  register() {
    const user = {
      name: this.name,
      email: this.email,
      password: this.password
    };

    localStorage.setItem('user', JSON.stringify(user));
    alert('Registered Successfully');
    window.location.href = '/login';
  }
}