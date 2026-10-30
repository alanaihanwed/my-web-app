from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>برنامه‌ریز هوشمند من 😁</title>
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;700;900&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Vazirmatn', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: #fff;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 40px 20px;
        }
        .container {
            width: 100%;
            max-width: 750px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        }

        /* --- ساعت مشتی --- */
        .clock-box {
            text-align: center;
            margin-bottom: 30px;
            padding: 25px;
            background: linear-gradient(135deg, rgba(0, 242, 254, 0.08), rgba(79, 172, 254, 0.02));
            border: 1px solid rgba(0, 242, 254, 0.2);
            border-radius: 20px;
            position: relative;
            overflow: hidden;
        }
        .clock-box::before {
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: radial-gradient(circle, rgba(0, 242, 254, 0.15), transparent 60%);
            animation: pulse 4s infinite;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 0.8; }
        }
        .clock-time {
            font-size: 3.5rem;
            font-weight: 900;
            font-family: 'Vazirmatn', sans-serif;
            letter-spacing: 2px;
            background: linear-gradient(90deg, #00f2fe, #4facfe, #00f2fe);
            background-size: 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shine 3s linear infinite;
            position: relative;
            z-index: 1;
        }
        @keyframes shine {
            0% { background-position: 0%; }
            100% { background-position: 200%; }
        }
        .clock-date {
            font-size: 1.1rem;
            color: #aaa;
            margin-top: 5px;
            position: relative;
            z-index: 1;
        }
        /* ------------- */

        h1 {
            text-align: center;
            font-size: 2rem;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #00f2fe, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 30px;
            font-size: 0.95rem;
        }
        .input-group {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 30px;
        }
        .input-row {
            display: flex;
            gap: 10px;
        }
        .input-group input, .input-group select {
            flex: 1;
            padding: 14px 18px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: #fff;
            font-family: inherit;
            font-size: 0.95rem;
            outline: none;
            transition: border 0.3s;
        }
        .input-group input:focus, .input-group select:focus {
            border-color: #00f2fe;
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.2);
        }
        .input-group input::placeholder { color: #666; }
        input[type="date"], input[type="time"] {
            color-scheme: dark;
        }
        .input-group button {
            padding: 15px 30px;
            background: linear-gradient(90deg, #00f2fe, #4facfe);
            border: none;
            border-radius: 12px;
            color: #05050a;
            font-family: inherit;
            font-weight: 700;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s;
        }
        .input-group button:hover {
            transform: scale(1.03);
            box-shadow: 0 10px 30px rgba(0, 242, 254, 0.4);
        }
        .filter-row {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .filter-btn {
            padding: 8px 18px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 50px;
            color: #aaa;
            font-family: inherit;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.3s;
        }
        .filter-btn.active, .filter-btn:hover {
            background: rgba(0, 242, 254, 0.15);
            border-color: #00f2fe;
            color: #00f2fe;
        }
        .stats {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
        }
        .stats div { text-align: center; }
        .stats .num { font-size: 1.5rem; font-weight: 900; color: #00f2fe; }
        .stats .label { font-size: 0.85rem; color: #888; }
        ul { list-style: none; }
        li {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 18px 20px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            margin-bottom: 12px;
            transition: all 0.3s;
            animation: slideIn 0.4s ease;
            border-right: 4px solid transparent;
        }
        li.priority-high { border-right-color: #ff4757; }
        li.priority-medium { border-right-color: #ffa502; }
        li.priority-low { border-right-color: #00f2fe; }
        li:hover {
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(0, 242, 254, 0.3);
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-30px); }
            to { opacity: 1; transform: translateX(0); }
        }
        li.done { opacity: 0.6; }
        li.done .task-text { text-decoration: line-through; color: #666; }
        .checkbox {
            width: 24px; height: 24px;
            border: 2px solid #4facfe;
            border-radius: 50%;
            cursor: pointer;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }
        .checkbox.checked {
            background: #00f2fe;
            border-color: #00f2fe;
        }
        .checkbox.checked::after {
            content: '✓';
            color: #05050a;
            font-weight: 900;
            font-size: 1rem;
        }
        .task-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        .task-text { font-size: 1rem; word-break: break-word; }
        .task-meta {
            display: flex;
            gap: 15px;
            font-size: 0.8rem;
            color: #888;
            flex-wrap: wrap;
        }
        .task-meta span { display: flex; align-items: center; gap: 4px; }
        .overdue { color: #ff4757 !important; font-weight: 700; }
        .delete-btn {
            background: transparent;
            border: none;
            color: #ff4757;
            font-size: 1.3rem;
            cursor: pointer;
            padding: 5px 10px;
            border-radius: 8px;
            transition: all 0.3s;
            opacity: 0.6;
        }
        .delete-btn:hover {
            background: rgba(255, 71, 87, 0.15);
            opacity: 1;
            transform: scale(1.2);
        }
        .empty { text-align: center; color: #666; padding: 40px; font-size: 1.1rem; }
        .clear-btn {
            display: block;
            margin: 25px auto 0;
            padding: 12px 30px;
            background: transparent;
            border: 1px solid rgba(255, 71, 87, 0.4);
            border-radius: 12px;
            color: #ff4757;
            font-family: inherit;
            cursor: pointer;
            transition: all 0.3s;
        }
        .clear-btn:hover { background: rgba(255, 71, 87, 0.1); border-color: #ff4757; }
        @media (max-width: 600px) {
            .container { padding: 25px 20px; }
            h1 { font-size: 1.5rem; }
            .input-row { flex-direction: column; }
            .clock-time { font-size: 2.2rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="clock-box">
            <div class="clock-time" id="clockTime">00:00:00</div>
            <div class="clock-date" id="clockDate">در حال بارگذاری...</div>
        </div>

        <h1>📅 برنامه‌ریز هوشمند من</h1>
        <p class="subtitle">کارهایت را برای تاریخ و ساعت مشخص برنامه‌ریزی کن!</p>

        <div class="input-group">
            <input type="text" id="taskInput" placeholder="عنوان کار (مثلاً جلسه کاری)..." onkeypress="if(event.key==='Enter') addTask()">
            <div class="input-row">
                <input type="date" id="taskDate" title="تاریخ">
                <input type="time" id="taskTime" title="ساعت">
                <select id="taskPriority" title="اولویت">
                    <option value="low">🟢 اولویت کم</option>
                    <option value="medium" selected>🟡 اولویت متوسط</option>
                    <option value="high">🔴 اولویت بالا</option>
                </select>
            </div>
            <button onclick="addTask()">افزودن به برنامه +</button>
        </div>

        <div class="filter-row">
            <button class="filter-btn active" onclick="setFilter('all', this)">همه</button>
            <button class="filter-btn" onclick="setFilter('today', this)">امروز</button>
            <button class="filter-btn" onclick="setFilter('upcoming', this)">آینده</button>
            <button class="filter-btn" onclick="setFilter('done', this)">انجام شده</button>
        </div>

        <div class="stats">
            <div><div class="num" id="totalCount">0</div><div class="label">کل</div></div>
            <div><div class="num" id="doneCount">0</div><div class="label">انجام شده</div></div>
            <div><div class="num" id="leftCount">0</div><div class="label">باقی‌مانده</div></div>
        </div>

        <ul id="taskList"></ul>

        <button class="clear-btn" onclick="clearDone()">پاک کردن کارهای انجام‌شده 🗑️</button>
    </div>

    <script>
        let tasks = JSON.parse(localStorage.getItem('smartTasks') || '[]');
        let currentFilter = 'all';

        // --- ساعت مشتی ---
        function updateClock() {
            const now = new Date();
            
            // ساعت با فرمت 12 ساعته
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            const timeStr = `${hours}:${minutes}:${seconds}`;
            
            // تاریخ شمسی
            const dateStr = now.toLocaleDateString('fa-IR', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
            
            document.getElementById('clockTime').textContent = timeStr;
            document.getElementById('clockDate').textContent = dateStr;
        }
        
        setInterval(updateClock, 1000);
        updateClock();
        // -----------------

        function save() {
            localStorage.setItem('smartTasks', JSON.stringify(tasks));
        }

        function setFilter(filter, btn) {
            currentFilter = filter;
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            render();
        }

        function isToday(dateStr) {
            if (!dateStr) return false;
            const today = new Date().toISOString().split('T')[0];
            return dateStr === today;
        }

        function isUpcoming(dateStr) {
            if (!dateStr) return false;
            const today = new Date().toISOString().split('T')[0];
            return dateStr > today;
        }

        function isOverdue(task) {
            if (!task.date || task.done) return false;
            const now = new Date();
            const taskDateTime = new Date(task.date + 'T' + (task.time || '23:59'));
            return taskDateTime < now;
        }

        function render() {
            const list = document.getElementById('taskList');
            list.innerHTML = '';

            let filtered = tasks.filter(task => {
                if (currentFilter === 'done') return task.done;
                if (currentFilter === 'today') return isToday(task.date) && !task.done;
                if (currentFilter === 'upcoming') return isUpcoming(task.date) && !task.done;
                return true;
            });

            filtered.sort((a, b) => {
                const dateA = new Date((a.date || '9999-99-99') + 'T' + (a.time || '99:99'));
                const dateB = new Date((b.date || '9999-99-99') + 'T' + (b.time || '99:99'));
                return dateA - dateB;
            });

            if (filtered.length === 0) {
                list.innerHTML = '<div class="empty">هیچ کاری در این بخش وجود ندارد! ✨</div>';
            } else {
                filtered.forEach((task) => {
                    const index = tasks.indexOf(task);
                    const li = document.createElement('li');
                    if (task.done) li.classList.add('done');
                    if (task.priority) li.classList.add('priority-' + task.priority);

                    const overdue = isOverdue(task);

                    li.innerHTML = `
                        <div class="checkbox ${task.done ? 'checked' : ''}" onclick="toggleTask(${index})"></div>
                        <div class="task-content">
                            <span class="task-text">${task.text}</span>
                            <div class="task-meta">
                                ${task.date ? `<span class="${overdue ? 'overdue' : ''}">📅 ${task.date}</span>` : ''}
                                ${task.time ? `<span class="${overdue ? 'overdue' : ''}">⏰ ${task.time}</span>` : ''}
                            </div>
                        </div>
                        <button class="delete-btn" onclick="deleteTask(${index})">✕</button>
                    `;
                    list.appendChild(li);
                });
            }

            document.getElementById('totalCount').textContent = tasks.length;
            document.getElementById('doneCount').textContent = tasks.filter(t => t.done).length;
            document.getElementById('leftCount').textContent = tasks.filter(t => !t.done).length;
        }

        function addTask() {
            const input = document.getElementById('taskInput');
            const text = input.value.trim();
            if (!text) return;

            tasks.push({
                text: text,
                date: document.getElementById('taskDate').value,
                time: document.getElementById('taskTime').value,
                priority: document.getElementById('taskPriority').value,
                done: false
            });

            input.value = '';
            document.getElementById('taskDate').value = '';
            document.getElementById('taskTime').value = '';
            save();
            render();
        }

        function toggleTask(index) {
            tasks[index].done = !tasks[index].done;
            save();
            render();
        }

        function deleteTask(index) {
            tasks.splice(index, 1);
            save();
            render();
        }

        function clearDone() {
            tasks = tasks.filter(t => !t.done);
            save();
            render();
        }

        render();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
