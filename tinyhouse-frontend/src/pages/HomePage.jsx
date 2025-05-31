import Navbar from '../components/Navbar';

const HomePage = () => (
  <>
    <Navbar isLoginPage={false} />

    {/* Hero (kayan görsel alanı) */}
    <section className="w-full h-[400px] bg-gray-200 flex items-center justify-center">
      <h2 className="text-4xl font-bold text-gray-700">Kayan Görsel Alanı (Slider)</h2>
    </section>

    {/* Öne Çıkan Özellikler */}
    <section className="py-12 px-4 bg-white">
      <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
        <div className="p-6 border rounded-lg shadow text-center">
          <h3 className="text-xl font-semibold mb-2">Doğa ile İç İçe</h3>
          <p>En güzel tiny house deneyimleri sizi bekliyor.</p>
        </div>
        <div className="p-6 border rounded-lg shadow text-center">
          <h3 className="text-xl font-semibold mb-2">Kolay Rezervasyon</h3>
          <p>Sade ve hızlı kullanıcı deneyimi.</p>
        </div>
        <div className="p-6 border rounded-lg shadow text-center">
          <h3 className="text-xl font-semibold mb-2">Uygun Fiyatlar</h3>
          <p>Her bütçeye uygun tatil çözümleri.</p>
        </div>
      </div>
    </section>
  </>
);

export default HomePage;
