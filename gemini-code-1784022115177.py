import os
import webbrowser

# كود صفحة الويب HTML/CSS بالكامل تم تخزينه داخل متغير نصي
html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>درع الأمان - تطبيق الحماية الشبحي الخارق</title>
    <style>
        :root {
            --primary: #ff3333;
            --primary-hover: #cc0000;
            --dark: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --text-muted: #94a3b8;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--dark);
            color: var(--text);
            line-height: 1.6;
        }

        header {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .hero {
            max-width: 1000px;
            margin: 4rem auto;
            text-align: center;
            padding: 0 1rem;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            color: #fff;
        }

        .hero h1 span {
            color: var(--primary);
        }

        .hero p {
            font-size: 1.25rem;
            color: var(--text-muted);
            max-width: 700px;
            margin: 0 auto 2rem auto;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 4rem auto;
            padding: 0 1rem;
        }

        .feature-card {
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid #334155;
            transition: transform 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-card h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: #fff;
        }

        .feature-card p {
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        .pricing-section {
            max-width: 1200px;
            margin: 6rem auto;
            padding: 0 1rem;
            text-align: center;
        }

        .pricing-section h2 {
            font-size: 2.5rem;
            margin-bottom: 3rem;
        }

        .pricing-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
            align-items: stretch;
        }

        .price-card {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 3rem 2rem;
            width: 320px;
            border: 1px solid #334155;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }

        .price-card.popular {
            border: 2px solid var(--primary);
            transform: scale(1.05);
        }

        .badge {
            position: absolute;
            top: -15px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--primary);
            color: #fff;
            padding: 0.25rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: bold;
        }

        .price-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .price {
            font-size: 2.5rem;
            font-weight: bold;
            color: #fff;
            margin-bottom: 1.5rem;
        }

        .price span {
            font-size: 1rem;
            color: var(--text-muted);
        }

        .price-features {
            list-style: none;
            margin-bottom: 2rem;
            text-align: right;
        }

        .price-features li {
            margin-bottom: 0.75rem;
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        .price-features li::before {
            content: "✓ ";
            color: var(--primary);
            font-weight: bold;
            margin-left: 0.5rem;
        }

        .btn {
            display: block;
            background: #334155;
            color: #fff;
            text-decoration: none;
            padding: 0.8rem;
            border-radius: 8px;
            font-weight: bold;
            transition: background 0.3s;
        }

        .price-card.popular .btn {
            background: var(--primary);
        }

        .price-card.popular .btn:hover {
            background: var(--primary-hover);
        }

        .btn:hover {
            background: #475569;
        }

        footer {
            text-align: center;
            padding: 3rem 1rem;
            color: var(--text-muted);
            border-top: 1px solid #334155;
            max-width: 1200px;
            margin: 0 auto;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2rem; }
            .price-card.popular { transform: scale(1); }
            .pricing-container { flex-direction: column; align-items: center; }
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">🛡️ درع الأمان / CyberShield</div>
    </header>

    <section class="hero">
        <h1>احمِ خصوصيتك وبياناتك بـ <span>درع شبحي خارق</span></h1>
        <p>تطبيق حماية متطور لأجهزة الكمبيوتر، يعمل بأداء فائق الخفة ومستند إلى السحاب لتدمير الفيروسات وبرمجيات الفدية قبل أن تلمس ملفاتك.</p>
    </section>

    <section class="features">
        <div class="feature-card">
            <h3>⚡ خفيف كالشبح</h3>
            <p>برمجة محسنة بالكامل تعتمد على فحص الـ Hash محلياً، مما يضمن حماية قصوى واستهلاكاً يقارب 0% من المعالج والذاكرة.</p>
        </div>
        <div class="feature-card">
            <h3>☁️ استخبارات سحابية</h3>
            <p>مرتبط مباشرة بأحدث خوادم Google Cloud ومحركات الفحص العالمية لتحديث حمايتك ضد التهديدات الجديدة لحظة بلحظة.</p>
        </div>
        <div class="feature-card">
            <h3>🔒 خصوصية مطلقة</h3>
            <p>درع متكامل لقفل كاميرا الويب والميكروفون، وحماية الحافظة (Copy-Paste) من برامج التجسس وسرقة الحسابات البنكية.</p>
        </div>
    </section>

    <section class="pricing-section">
        <h2>اختر خطة الحماية الأنسب لك</h2>
        <div class="pricing-container">
            
            <div class="price-card">
                <div>
                    <h3>الاشتراك الأسبوعي</h3>
                    <div class="price">$9.99<span> / أسبوعياً</span></div>
                    <ul class="price-features">
                        <li>حماية كاملة في الوقت الفعلي</li>
                        <li>فحص سحابي للمواقف الحرجة</li>
                    </ul>
                </div>
                <a href="#" class="btn">اشترك الآن</a>
            </div>

            <div class="price-card popular">
                <div class="badge">الأكثر مبيعاً ⭐</div>
                <div>
                    <h3>الاشتراك الشهري الاحترافي</h3>
                    <div class="price">$19.99<span> / شهرياً</span></div>
                    <ul class="price-features">
                        <li>توفير ضخم مقارنة بالحزمة الأسبوعية</li>
                        <li>دروع الخصوصية (الكاميرا والمايك)</li>
                        <li>تحديثات سحابية فورية صامتة</li>
                        <li>دعم فني ذكي متواصل</li>
                    </ul>
                </div>
                <a href="#" class="btn">اشترك بـ Apple Pay</a>
            </div>

            <div class="price-card">
                <div>
                    <h3>الاشتراك السنوي</h3>
                    <div class="price">$149.99<span> / سنوياً</span></div>
                    <ul class="price-features">
                        <li>الوصول الكامل لكافة ميزات النظام</li>
                        <li>حماية ممتدة لـ 12 شهراً كاملة</li>
                        <li>توفير مالي للمدى الطويل</li>
                    </ul>
                </div>
                <a href="#" class="btn">اشترك الآن</a>
            </div>

        </div>
    </section>

    <footer>
        <p>🔒 جميع المدفوعات مشفرة وآمنة 100%. نضمن استرجاع الأموال خلال 7 أيام إذا لم يعجبك التطبيق.</p>
        <p style="margin-top: 1rem;">&copy; 2026 درع الأمان. جميع الحقوق محفوظة.</p>
    </footer>

</body>
</html>"""

# اسم ملف الويب المخرَج
file_name = "index.html"

# فتح الملف يدويًا وحقن كود الويب بداخله بصيغة UTF-8 ليدعم اللغة العربية بشكل سليم
with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"[+] تم إنشاء ملف الويب بنجاح باسم: {file_name}")

# الخدعة البرمجية الذكية: فتح الملف تلقائيًا في المتصفح فوراً بعد إنشائه
webbrowser.open('file://' + os.path.realpath(file_name))
print("[+] تم فتح صفحة البيع الآن على متصفحك الافتراضي!")
