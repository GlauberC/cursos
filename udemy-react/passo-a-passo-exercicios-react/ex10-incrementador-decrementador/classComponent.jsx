import React, {Component} from 'react'

export default class ClassComponent extends Component{
  constructor(props){
    super(props)
    this.state = {value: props.initialValue}
  }//constructor
  sum(delta){
    this.setState({value: this.state.value + delta})
  }


  render(){
    //this.props.value++ Não consegue alterar, pois no react os componentes são somente leitura
    return(
      <div>
        <h1>{this.props.label}</h1>
        <h2>{this.state.value}</h2>
        <button onClick={() => this.sum(-1)}>Dec</button>
        <button onClick={() => this.sum(1)}>Inc</button>
      </div>
    )//return
  }//render
}//ClassComponent
