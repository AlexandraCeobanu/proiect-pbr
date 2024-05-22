import { useState } from 'react';
import './App.css';
import { solve } from './sendPremises';

function App() {
  const [majorPremise, setMajorPremise] = useState("")
  const [minorPremise, setMinorPremise] = useState("")
  const [conclusion, setConclusion] = useState(null)
  const [selectedValueMajor, setSelectedValueMajor] = useState("All");
  const [selectedValueMinor, setSelectedValueMinor] = useState("All");
  const [error, setError] = useState(null)
  const handleChangeMajorPremise = (event) => {
    setMajorPremise(event.target.value);
  }
  const handleChangeMinorPremise = (event) => {
    setMinorPremise(event.target.value);
  }
  const handleSubmitPremises = (event) => {
    event.preventDefault()
    let premises = [{
      type: selectedValueMajor,
      sentence: majorPremise
    },
    {
      type: selectedValueMinor,
      sentence: minorPremise
    }]
    
    solve(premises)
    .then((response) => {
      console.log(response)
      setConclusion(response)
      setError(null)
    })
    .catch((error) => {
      setConclusion(null);
      setError(error);
    })
  }
  const handleChangeSelectMajor = (event) => {
    setSelectedValueMajor(event.target.value)
  }
  const handleChangeSelectMinor = (event) => {
    setSelectedValueMinor(event.target.value)
  }
  return (
    <div className="App">
      <h1>Syllogism solver</h1>
      <form onSubmit={handleSubmitPremises}>
      <div className='premise'>
      <label>Major premise</label>

      <div className='premise-block'>
      <select id="select" value={selectedValueMajor} onChange={handleChangeSelectMajor}>
        <option value="All">All</option>
        <option value="Some">Some</option>
        <option value="No">No</option>
        <option value="(empty)">(empty)</option>
      </select>
      <input type="text" id="major-premise" name ="major-premise" required onChange={handleChangeMajorPremise}></input>
      </div>
      </div>
      <div className='premise'>
      <label >Minor premise</label>
      <div className='premise-block'>
      <select id="select" value={selectedValueMinor} onChange={handleChangeSelectMinor}>
        <option value="All">All</option>
        <option value="Some">Some</option>
        <option value="No">No</option>
        <option value="(empty)">(empty)</option>
      </select>
      <input type="text" id="major-premise" name ="minor-premise" required onChange={handleChangeMinorPremise}></input>
      </div>
      </div>
      {conclusion !== null &&
        <h3>Conclusion : {conclusion}</h3>
        }
        {error !== null &&
        <h3>Error : {error}</h3>
        }
      <button style={{ marginTop: conclusion || error ? '1.5em' : '5em' }} type="submit" id="submit" name="submit" value="Login">Generate Conclusion</button>
      </form>
    </div>
  );
}

export default App;
