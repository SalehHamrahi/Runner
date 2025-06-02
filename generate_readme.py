import os
from pathlib import Path

def parse_results(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    start_idx = 0
    for i, line in enumerate(lines):
        if '----' in line:
            start_idx = i + 1
            break
    
    teams = []
    for line in lines[start_idx:]:
        if not line.strip():
            continue
        parts = line.split()
        team_name = ' '.join(parts[1:-7])
        stats = parts[-7:]
        teams.append({
            'position': parts[0],
            'name': team_name,
            'wins': stats[0],
            'draws': stats[1],
            'losses': stats[2],
            'goals_for': stats[3],
            'goals_against': stats[4],
            'goal_difference': stats[5],
            'points': stats[6]
        })
    
    return teams

def generate_readme(results_path, network_img_path, stats_img_path):
    Path("./Analysis_Results").mkdir(parents=True, exist_ok=True)
    teams = parse_results(results_path)
    
    table_header = "| Pos | Team | W | D | L | GF | GA | GD | P |\n"
    table_header += "|-----|------|---|---|---|----|----|----|---|\n"
    
    table_rows = ""
    for team in teams:
        row = f"| {team['position']} | {team['name']} | {team['wins']} | {team['draws']} | {team['losses']} | "
        row += f"{team['goals_for']} | {team['goals_against']} | {team['goal_difference']} | {team['points']} |\n"
        table_rows += row

    readme_content = f"""# نتایج جام قهرمانی فوتبال

## جدول رده‌بندی

{table_header}{table_rows}

## تحلیل شبکه نتایج
![شبکه نتایج مسابقات]({network_img_path})

## آمار عملکرد تیم‌ها
![آمار تیم‌ها]({stats_img_path})

### توضیحات تحلیل‌ها
- **نمودار شبکه مسابقات**:
  - فلش‌های سیاه: نشان‌دهنده برد تیم مبدأ مقابل تیم مقصد
  - خطوط آبی: نشان‌دهنده بازی‌های مساوی
  - جهت فلش‌ها نشان‌دهنده تیم برنده است

- **نمودار آماری**:
  - مقایسه عملکرد تیم‌ها بر اساس برد/مساوی/باخت
  - آنالیز تفاضل گل و امتیازات کسب‌شده

"""

    with open("README_Analiz.md", "w", encoding="utf-8") as file:
        file.write(readme_content.strip())

if __name__ == "__main__":
    results_path = "./Results.txt"
    network_img_path = "./Analysis_Results/match_network_colored.png"
    stats_img_path = "./Analysis_Results/team_stats_chart.png"
    
    generate_readme(results_path, network_img_path, stats_img_path)
