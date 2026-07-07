from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import getpass
import sys

from strength import check_strength
from breach_check import check_breach

console = Console()

def estimate_crack_time(entropy):
    """Estimate time to crack assuming 1 billion guesses/sec"""
    if entropy == 0:
        return "Instantly"
    guesses = 2 ** entropy
    seconds = guesses / 1_000_000_000
    if seconds < 1: return "Instantly"
    if seconds < 60: return f"{seconds:.1f} seconds"
    if seconds < 3600: return f"{seconds/60:.1f} minutes"
    if seconds < 86400: return f"{seconds/3600:.1f} hours"
    if seconds < 31536000: return f"{seconds/86400:.1f} days"
    if seconds < 31536000 * 1000: return f"{seconds/31536000:.1f} years"
    return f"{(seconds/31536000)/1e9:.1f} billion years"

def analyze_password(password):
    """Run full analysis"""
    
    console.print(Panel.fit(
        f"[bold cyan]🔐 Analyzing Password[/bold cyan]",
        border_style="cyan"
    ))
    
    # Strength check
    strength = check_strength(password)
    
    table = Table(box=box.ROUNDED, title="📊 Strength Report")
    table.add_column("Metric", style="bold yellow")
    table.add_column("Value", style="white")
    
    table.add_row("Rating", strength["rating"])
    table.add_row("Score", f"{strength['score']} / 9")
    table.add_row("Entropy", f"{strength['entropy']} bits")
    table.add_row("Crack Time (est.)", estimate_crack_time(strength['entropy']))
    table.add_row("Length", str(len(password)))
    
    console.print(table)
    
    # Feedback
    if strength["feedback"]:
        console.print("\n[bold yellow]💡 Suggestions:[/bold yellow]")
        for tip in strength["feedback"]:
            console.print(f"  {tip}")
    else:
        console.print("\n[bold green]✅ Great password![/bold green]")
    
    # Breach check
    console.print("\n[bold cyan]🌐 Checking breach database...[/bold cyan]")
    breach = check_breach(password)
    
    if "error" in breach:
        console.print(f"[red]Error: {breach['error']}[/red]")
    else:
        if breach["breached"]:
            console.print(Panel(
                f"[bold red]{breach['message']}[/bold red]\n"
                f"[red]DO NOT use this password![/red]",
                border_style="red"
            ))
        else:
            console.print(Panel(
                f"[bold green]{breach['message']}[/bold green]",
                border_style="green"
            ))

def main():
    console.print(Panel.fit(
        "[bold cyan]🔐 Password Strength Analyzer & Breach Checker[/bold cyan]\n"
        "[dim]Built with Python | Uses Have I Been Pwned API[/dim]",
        border_style="cyan"
    ))
    
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = getpass.getpass("\nEnter password to analyze: ")
    
    analyze_password(password)

if __name__ == "__main__":
    main()
