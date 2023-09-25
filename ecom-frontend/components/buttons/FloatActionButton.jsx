
import { InboxIcon } from '@heroicons/react/24/solid'

export default function FloatActionButton(props) {
    const { onClick } = props
    return (
        <button
            className="fixed z-90 bottom-10 right-8 bg-blue-600 w-20 h-20 rounded-full drop-shadow-lg flex 
            justify-center items-center text-white text-4xl hover:bg-blue-700 hover:drop-shadow-2xl transition-all
            "
            onClick={onClick}
        >
            <InboxIcon className='h-6 w-6' />
        </button>
    )
}