# src/visualization.py
import matplotlib.pyplot as plt

def plot_commits_per_month(series):
    series.sort_index().plot(kind='line')
    plt.title('Commits mỗi tháng')
    plt.xlabel('Năm, Tháng')
    plt.ylabel('Số lượng Commit')
    plt.tight_layout()
    plt.savefig("plot_commits_per_month.png")
    plt.show()

def plot_top_authors(series):
    series.plot(kind='bar')
    plt.title('Top Authors theo số lượng Commit')
    plt.xlabel('Author')
    plt.ylabel('Commits')
    plt.tight_layout()
    plt.savefig("plot_top_authors.png")
    plt.show()


def plot_commit_type_ratio(series):
    series.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Commits theo loại')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("plot_commit_type_ratio.png")
    plt.show()

def plot_message_length(stats, length_category):

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Biểu đồ: Phân bố theo category
    colors = ['#3498db', '#9b59b6', '#2ecc71', '#e67e22', '#e74c3c']
    length_category.plot(kind='bar', ax=ax, color=colors)
    ax.set_title('Phân bố độ dài Commit Message')
    ax.set_xlabel('Phân loại độ dài')
    ax.set_ylabel('Số lượng commit')
    ax.tick_params(axis='x', rotation=45)
    
    # Thêm text box hiển thị thống kê
    stats_text = f"Thống kê:\n" \
                 f"• Trung bình: {stats['mean']:.1f} ký tự\n" \
                 f"• Trung vị: {stats['median']:.1f} ký tự\n" \
                 f"• Độ lệch chuẩn: {stats['std']:.1f}\n" \
                 f"• Min: {stats['min']} | Max: {stats['max']}"
    
    ax.text(0.98, 0.95, stats_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig("plot_message_length.png")
    plt.show()

def plot_commits_by_time(hourly_commits, time_frame_commits):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Biểu đồ 1: Commit theo từng giờ
    hourly_commits.plot(kind='bar', ax=axes[0], color='coral')
    axes[0].set_title('Tần suất Commit theo Giờ')
    axes[0].set_xlabel('Giờ trong ngày')
    axes[0].set_ylabel('Số lượng commit')
    
    # Biểu đồ 2: Commit theo khung giờ
    colors = ['#f1c40f', '#e67e22', '#9b59b6', '#34495e']
    time_frame_commits.plot(kind='pie', ax=axes[1], autopct='%1.1f%%', colors=colors)
    axes[1].set_title('Tần suất Commit theo Khung giờ')
    axes[1].set_ylabel('')
    
    plt.tight_layout()
    plt.savefig("plot_commits_by_time.png")
    plt.show()
