import axios from 'axios';
const config = {
    headers: {
      'Content-Type': 'application/json', 
    }

  };
export const solve = async (premises) => {
    try{
        const response = await axios.post(`http://localhost:8000/solve`,premises,config);
        if(response.status === 200)
        {
            const conclusion = await response.data;
            
        }
    }
    catch (error) {
        console.log(`Failed to get conclusion.`,error);
        throw error.response.data;
    }
};