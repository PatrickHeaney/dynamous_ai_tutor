"""The command-line interface for the AI agent."""

import typer
from rich.console import Console
from rich.prompt import Prompt

from .agent import AgentCore

app = typer.Typer()
console = Console()


@app.command()
def main():
    """
    Starts the AI agent's conversational loop.
    """
    try:
        agent = AgentCore()
        console.print(
            "[bold green]Welcome to the AI Assistant! "
            "Type 'exit' or press Ctrl+C to end.[/bold green]"
        )

        while True:
            user_input = Prompt.ask("[bold blue]You[/bold blue]")

            if user_input.lower() == "exit":
                break

            console.print("[bold yellow]Assistant[/bold yellow]: ", end="")
            with console.status("Thinking...", spinner="dots"):
                response_content = agent.chat(user_input)
                if response_content:
                    console.print(response_content)

    except (KeyboardInterrupt, EOFError):
        console.print("\n[bold red]Exiting gracefully.[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]An error occurred: {e}[/bold red]")


if __name__ == "__main__":
    app()
