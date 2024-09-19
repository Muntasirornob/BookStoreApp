import {AllRoutes} from './routes/AllRoutes';
import {Footer,Header} from './components/layouts';


function App() {
  return (

    <div className='App'>
      <Header/>
        <AllRoutes/>
      <Footer/>


    </div>


  )
  
}

export default App