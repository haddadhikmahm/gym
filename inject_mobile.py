import os

files = [
    'd:/aagym/a_a_gym_landing_page.html',
    'd:/aagym/a_a_gym_gallery.html',
    'd:/aagym/a_a_gym_self_registration.html',
    'd:/aagym/a_a_gym_fmbg.html',
    'd:/aagym/a_a_gym_check_member.html'
]

mobile_menu_html = """
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="fixed inset-0 bg-[#0a0a0a]/95 backdrop-blur-xl z-[100] transform translate-x-full transition-transform duration-500 flex flex-col lg:hidden">
        <div class="flex justify-between items-center p-6 border-b border-gray-800">
            <div class="flex items-center gap-3">
                <img src="logo%20gym.jpg" alt="A.A Gym Logo" class="h-10 w-10 rounded-full object-cover">
                <span class="text-xl font-black italic tracking-tighter text-white">A.A <span class="text-aagreen">GYM</span></span>
            </div>
            <button id="close-menu" class="text-gray-400 hover:text-white text-3xl focus:outline-none transition">
                <i class="fas fa-times"></i>
            </button>
        </div>
        <div class="flex-grow flex flex-col p-6 overflow-y-auto space-y-4">
            <a href="a_a_gym_landing_page.html" class="text-2xl font-bold text-white hover:text-aagreen transition py-2 border-b border-gray-800">Beranda</a>
            <a href="a_a_gym_self_registration.html" class="text-2xl font-bold text-white hover:text-aagreen transition py-2 border-b border-gray-800">Membership</a>
            <a href="a_a_gym_gallery.html" class="text-2xl font-bold text-white hover:text-aagreen transition py-2 border-b border-gray-800">Galeri</a>
            
            <div class="py-2 border-b border-gray-800 flex flex-col gap-3">
                <span class="text-sm font-semibold text-gray-500 uppercase tracking-widest">Pembaruan</span>
                <a href="a_a_gym_check_member.html" class="text-xl font-bold text-gray-300 hover:text-white flex items-center gap-2"><i class="fas fa-id-card text-aagreen w-6"></i> Cek Member</a>
                <a href="a_a_gym_fmbg.html" class="text-xl font-bold text-gray-300 hover:text-white flex items-center gap-2"><i class="fas fa-shield-alt text-aagreen w-6"></i> Program Garansi</a>
                <a href="a_a_gym_self_registration.html" class="text-xl font-bold text-gray-300 hover:text-white flex items-center gap-2"><i class="fas fa-tags text-aagreen w-6"></i> Promo Menarik</a>
            </div>

            <div class="py-2 border-b border-gray-800 flex flex-col gap-3">
                <span class="text-sm font-semibold text-gray-500 uppercase tracking-widest">Kelas</span>
                <a href="a_a_gym_landing_page.html#kelas" class="text-xl font-bold text-gray-300 hover:text-white flex items-center gap-2"><i class="fas fa-dumbbell text-aagreen w-6"></i> Jadwal GX</a>
                <a href="a_a_gym_landing_page.html#kelas" class="text-xl font-bold text-gray-300 hover:text-white flex items-center gap-2"><i class="fas fa-burn text-aagreen w-6"></i> Jadwal Pilates+</a>
            </div>
            
            <a href="a_a_gym_landing_page.html#trainer" class="text-2xl font-bold text-white hover:text-aagreen transition py-2 border-b border-gray-800">Klub Kami</a>
            
            <div class="mt-6 mb-10">
                <a href="a_a_gym_self_registration.html" class="block text-center bg-aagreen text-aadark px-6 py-4 rounded-xl font-black text-lg shadow-[0_0_20px_rgba(57,255,20,0.4)] hover:bg-green-400 transition">
                    Gabung Sekarang
                </a>
            </div>
        </div>
    </div>
"""

mobile_js = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const mobileMenuBtn = document.getElementById('mobile-menu-btn');
            const closeMenuBtn = document.getElementById('close-menu');
            const mobileMenu = document.getElementById('mobile-menu');

            if (mobileMenuBtn && closeMenuBtn && mobileMenu) {
                mobileMenuBtn.addEventListener('click', () => {
                    mobileMenu.classList.remove('translate-x-full');
                });
                closeMenuBtn.addEventListener('click', () => {
                    mobileMenu.classList.add('translate-x-full');
                });
            }
        });
    </script>
"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update the button to have id="mobile-menu-btn"
    old_btn = '                <!-- Mobile Menu Button -->\n                <div class="lg:hidden flex items-center">\n                    <button class="text-gray-300 hover:text-white focus:outline-none">'
    new_btn = '                <!-- Mobile Menu Button -->\n                <div class="lg:hidden flex items-center">\n                    <button id="mobile-menu-btn" class="text-gray-300 hover:text-white focus:outline-none">'
    
    if old_btn in content:
        content = content.replace(old_btn, new_btn)
    
    # 2. Insert Mobile Menu HTML right after </nav>
    if 'id="mobile-menu"' not in content:
        content = content.replace('</nav>', '</nav>\n' + mobile_menu_html)
        
    # 3. Insert JS right before </body>
    if 'mobileMenuBtn.addEventListener' not in content:
        content = content.replace('</body>', mobile_js + '\n</body>')
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print('Done injecting mobile menu!')
