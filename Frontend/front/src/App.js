import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import {Container} from 'semantic-ui-react';
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      schools: null,
      people: null
    };
  }
  componentDidMount() {
    ["schools","people"].map((str) => {
      fetch(`http://10.229.139.63:8000/api/${str}/`).then(res => res.json()).then((result) => {
        this.setState({
          [str]: result
        });
      }, (error) => {
        console.log(error);
      })
    });
  }
  render() {
    const {schools, people} = this.state;
    if(!(schools && people)) return <Container>Loading...</Container>
    return (
      <Container>
        <h1>List of Schools</h1>
        { schools && 
          schools.map((school) => 
            <div>
              <h2 key={school.id}>
                {school.name}
              </h2>
              <div>{people.filter((person) => person.school === school.id)
                .map((person) => <div>{person.name}</div>)}
              </div>
            </div>
          )
        }
      </Container>
    );
  }
}

export default App;
