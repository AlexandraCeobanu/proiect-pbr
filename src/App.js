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
  const handleSubmitPremises = () => {
    let premises = [selectedValueMajor+ " " + majorPremise , selectedValueMinor + " " +  minorPremise]
    solve(premises)
    .then((response) => {
      setConclusion(response)
    })
    .catch((error) => {
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
        <option value="optiune1">All</option>
        <option value="optiune2">Some</option>
        <option value="optiune3">No</option>
      </select>
      <input type="text" id="major-premise" name ="major-premise" required onChange={handleChangeMajorPremise}></input>
      </div>
      </div>
      <div className='premise'>
      <label >Minor premise</label>
      <div className='premise-block'>
      <select id="select" value={selectedValueMinor} onChange={handleChangeSelectMinor}>
        <option value="optiune1">All</option>
        <option value="optiune2">Some</option>
        <option value="optiune3">No</option>
      </select>
      <input type="text" id="major-premise" name ="minor-premise" required onChange={handleChangeMinorPremise}></input>
      </div>
      </div>
      <button type="submit" id="submit" name="submit" value="Login">Generate Conclusion</button>
      </form>
      {conclusion !== null &&
       <div>
        <h2>Conclusion : {conclusion}</h2>
        </div>
        }
    </div>
  );
}

export default App;
