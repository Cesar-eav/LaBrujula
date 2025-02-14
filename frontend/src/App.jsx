import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import { AtractivosPage } from "./pages/AtractivosPage";
import { AscensoresPage } from "./pages/AscensoresPage";
import { IglesiasPage } from "./pages/IglesiasPage";
import { EscalerasPage } from "./pages/EscalerasPage";
import { HomePage } from "./pages/HomePage";
import { ArquitecturasPage } from "./pages/ArquitecturasPage";
import { MiradoresPage } from "./pages/MiradoresPage";
import { AtractivosFormPage } from "./pages/AtractivosFormPage";
import {Navigation} from './components/Navigation'
import Mapa from './components/Mapa'; 



function App() {
  return (
    <BrowserRouter>
    <Navigation />
      <Routes>
        {/* <Route path="/" element={<Navigate to="/atractivos" />} /> */}
        <Route path="/" element={<HomePage />} />
        <Route path="/atractivos" element={<AtractivosPage />} />
        <Route path="/atractivos-crear" element={<AtractivosFormPage />} />
        <Route path="/ascensores" element={<AscensoresPage />} />
        <Route path="/iglesias" element={<IglesiasPage />} />
        <Route path="/escaleras" element={<EscalerasPage />} />
        <Route path="/arquitectura" element={<ArquitecturasPage />} />
        <Route path="/miradores" element={<MiradoresPage />} />
        <Route path="/mapa/:lat/:lon" element={<Mapa />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
