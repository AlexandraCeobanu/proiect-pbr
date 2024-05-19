import axios from 'axios';
export const solve = async (premises) => {
    try{
        const response = await axios.post(`/solve`,premises);
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